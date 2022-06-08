# Created on Tue Jun 07 2022
#
# Copyright (c) 2022 EarthPlay

# Sample command for creating the sphere
python3 dynsphere/ -b https://dynmap.earthplay.de/ \
    --mintz -22 --maxtz 24 \
    --mintx -48 --maxtx 46 \
    --resx 2048 --resy 2048 \
    --tile-type zzzz_ \
    --tile-w 16 --tile-h 16 \
    --tile-dir tiles