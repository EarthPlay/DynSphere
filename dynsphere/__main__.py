#! /usr/bin/python3

# ________                 _________      .__                          
# \______ \ ___.__. ____  /   _____/_____ |  |__   ___________   ____  
#  |    |  <   |  |/    \ \_____  \\____ \|  |  \_/ __ \_  __ \_/ __ \ 
#  |    `   \___  |   |  \/        \  |_> >   Y  \  ___/|  | \/\  ___/ 
# /_______  / ____|___|  /_______  /   __/|___|  /\___  >__|    \___  >
#         \/\/         \/        \/|__|        \/     \/            \/ 
#
# DynSphere is a tool to create a spherical image of a Dynmap.
#
# It is licensed under the MIT license.
#
# (c) Copyright 2022 EarthPlay
#
# https://github.com/EarthPlay/DynSphere


import os, sys, colors

# The required modules
required_modules = [
    "argparse",
    "PIL"
]

for required in required_modules:
    try:
        __import__(required)
    except ImportError as e:
        print(
            f"{colors.red}ERROR{colors.reset} missing required module {required}: {e}"
        )
        print(
            f"{colors.yellow}WARNING{colors.reset} do you want to install the requirements from {os.getcwd()}/../requirements.txt?"
        )

        choice = input("[Y/n] ")

        if choice.lower() == "y":
            os.system(f"python3 -m pip install -r {os.getcwd()}/../requirements.txt")
        else:
            print(
                f"{colors.blue}INFO{colors.reset} please install the requirements manually."
            )
            sys.exit(1)


# Parse the commandline arguments
import commandline

commandline.parse()

# https://dynmap.earthplay.de/tiles/world/flat/6_1/zzzzz_192_32.jpg