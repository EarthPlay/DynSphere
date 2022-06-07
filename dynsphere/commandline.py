# Created on Tue Jun 07 2022
#
# Copyright (c) 2022 EarthPlay

import argparse, colors, logger, logging, generator
from settings import Settings

def silent_print_logo():
    """Print the logo if not in silent mode."""

    if not Settings.hide_logo:
        print_logo()


def print_logo():
    """Print the logo."""

    print(
        colors.format(
            """§o
________                 _________      .__                          
\______ \ ___.__. ____  /   _____/_____ |  |__   ___________   ____  
 |    |  <   |  |/    \ \_____  \\____ \|  |  \_/ __ \_  __ \_/ __ \ 
 |    `   \___  |   |  \/        \  |_> >   Y  \  ___/|  | \/\  ___/ 
/_______  / ____|___|  /_______  /   __/|___|  /\___  >__|    \___  >
        \/\/         \/        \/|__|        \/     \/            \/ 
    §R"""
        )
    )
    print(colors.format(f"DynSphere version §b{Settings.version}§R"))

    print("\n")
    print(
        colors.format(
            f"Written by §b{', '.join(Settings.authors)}§R \
licensed under §b{Settings.license}§R."
        )
    )
    print("")
    print(
        colors.format(
            f"§r(c)§R Copyright {Settings.year} \
§b{', '.join(Settings.authors)}§R"
        )
    )
    print("\n")


class help_formatter(argparse.HelpFormatter):
    """Custom help formatter."""

    def format_help(self):
        print_logo()
        return super().format_help() + "\n"

    def add_usage(self, usage, actions, groups, prefix=None):
        if usage is not argparse.SUPPRESS:
            self.add_text(
                f"{colors.blue}[USAGE]{colors.reset} {self._format_usage(usage, actions, groups, '')}"
            )


def parse():
    """Parse the commandline arguments."""

    parser = argparse.ArgumentParser(
        description="Process ReSVG files.", formatter_class=help_formatter
    )

    args = {
        "base-url;b": ["the base url", str],
        "no-color": ["disable color", "store_true"],
        "log": ["specify a log file", str],
        "level": ["specify a log level", int, 20],
        
        "mintx": ["minimum tile x coord", int, -15],
        "mintz": ["minimum tile z coord", int, -10],
        "maxtx": ["maximum tile x coord", int, 15],
        "maxtz": ["maximum tile z coord", int, 10],
        "resx": ["x resolution of output image", int, 768],
        "resy": ["y resolution of output image", int, 768],
        "world": ["maximum tile z coord", str, "world"],
        "tile-dir": ["directory where the tiles will be put in", str, "tiles"],
        "output;o": ["the output file", str, "sphere.png"],
        
        "silent;s": ["run in silent mode", "store_true"],
        "hide-logo": ["hide logo", "store_true"],
    }

    for arg, info in args.items():
        parts = arg.split(";")
        kwargs = {
            "help": info[0],
        }
        kwargs["action" if isinstance(info[1], str) else "type"] = info[1]
        kwargs["default"] = info[2] if len(info) > 2 else None
        kwargs["dest"] = parts[0].replace("-", "_")
        if len(parts) == 2:
            parser.add_argument(f"-{parts[1]}", f"--{parts[0]}", **kwargs)
        else:
            parser.add_argument(f"--{parts[0]}", **kwargs)

    args = parser.parse_args()

    Settings.silent = args.silent
    Settings.no_color = args.no_color
    Settings.hide_logo = args.silent or args.hide_logo
    Settings.base_url = args.base_url
    Settings.level = logging.ERROR if args.silent else args.level
    Settings.log = args.log
    Settings.mintx = args.mintx
    Settings.mintz = args.mintz
    Settings.maxtx = args.maxtx
    Settings.maxtz = args.maxtz
    Settings.world = args.world
    Settings.tile_dir = args.tile_dir
    Settings.output = args.output
    Settings.resx = args.resx
    Settings.resy = args.resy
    
    logger.setup_logger()

    if Settings.base_url:
        generator.generate()
    else:
        parser.print_help()