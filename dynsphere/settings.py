# Created on Tue Jun 07 2022
#
# Copyright (c) 2022 EarthPlay

class Settings:
    version = "0.0.0alpha0"
    authors = [
        "Earthplay",
    ]
    license = "MIT"
    year = "2022"
    
    tile_width: int = 16
    tile_height: int = 16
    
    tile_image_width: int = 128
    tile_image_height: int = 128
    
    tile_type: str
    
    output: str
    
    resx: int
    resy: int
    
    type: str
    
    base_url: str
    tile_dir: str
    world: str
    mintx: int
    mintz: int
    maxtx: int
    maxtz: int
    no_color: bool
    silent: bool
    hide_logo: bool
    log: str
    level: int
    