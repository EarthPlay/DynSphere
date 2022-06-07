# Created on Tue Jun 07 2022
#
# Copyright (c) 2022 EarthPlay

import logging
import math

import requests, os
from image_on_sphere import image_on_sphere
from settings import Settings

from PIL import Image

def generate():
    os.makedirs(Settings.tile_dir, exist_ok=True)
    
    tile_count_x = Settings.maxtx - Settings.mintx + 1
    tile_count_z = Settings.maxtz - Settings.mintz + 1
    
    width = Settings.tile_image_width * tile_count_x
    height = Settings.tile_image_height * tile_count_z
    image = Image.new("RGB", (width, height))
    
    logging.info("Generating from §o%s§R...", Settings.base_url)
    for tx in range(Settings.mintx, Settings.maxtx + 1):
        for tz in range(Settings.mintz, Settings.maxtz + 1):
            logging.info("Collecting tile tx: §o%s§R tz: §o%s§R...", tx, tz)
            other = collect_tile(tx, tz)
            boxx = (tx - Settings.mintx) * Settings.tile_image_width
            boxz = (tile_count_z - (tz - Settings.mintz) - 1) * Settings.tile_image_height
            logging.debug("Adding tile to image at §o%s§R §o%s§R...", boxx, boxz)
            image.paste(other, box=(boxx, boxz))
            other.close()

    full_location = f"{Settings.tile_dir}/full.jpg"
    
    logging.info("Saving full map to §o%s§R", full_location)
    image.save(full_location)
    
    logging.info("Generating spherical image")
    sphere = image_on_sphere(image, math.radians(-90),
                             math.radians(-90), math.radians(0),
                             Settings.resx, Settings.resy)
    
    logging.info("Saving sphere to §o%s§R", Settings.output)
    sphere.save(Settings.output)
    
    image.close()
    sphere.close()

            
    

def collect_tile(tx: int, tz: int) -> Image.Image:
    rtx = tx * Settings.tile_width
    rtz = tz * Settings.tile_height
    filename = f"{Settings.tile_dir}/{tx}_{tz}.jpg"
    if os.path.isfile(filename):
        logging.debug("Using already existing version of tile at §o%s§R.", filename)
    else:
        url = f"{Settings.base_url}tiles/{Settings.world}/flat/6_1/zzzzz_{rtx}_{rtz}.jpg"
        logging.debug("Downloading from §o%s§R...", url)
        res = requests.get(url)
        with open(filename, "wb") as f:
            f.write(res.content)
            
    return Image.open(filename)