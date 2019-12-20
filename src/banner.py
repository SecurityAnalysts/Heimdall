#!/usr/bin/env python3

import random

Version = "1.0"
Banner = random.randrange(3)

if Banner == 0:
    Banner = """
     _   _      _               _       _ _ 
    | | | | ___(_)_ __ ___   __| | __ _| | |
    | |_| |/ _ \ | '_ ` _ \ / _` |/ _` | | |
    |  _  |  __/ | | | | | | (_| | (_| | | |
    |_| |_|\___|_|_| |_| |_|\__,_|\__,_|_|_| Version: {}
""".format(Version)

elif Banner == 1:
    Banner = """
                _               _       _ _ 
      /\  /\___(_)_ __ ___   __| | __ _| | |
     / /_/ / _ \ | '_ ` _ \ / _` |/ _` | | |
    / __  /  __/ | | | | | | (_| | (_| | | |
    \/ /_/ \___|_|_| |_| |_|\__,_|\__,_|_|_| Version: {}
""".format(Version)

elif Banner == 2:
    Banner = """
     _   _      _               _       _ _ 
    | | | |    (_)             | |     | | |
    | |_| | ___ _ _ __ ___   __| | __ _| | |
    |  _  |/ _ \ | '_ ` _ \ / _` |/ _` | | |
    | | | |  __/ | | | | | | (_| | (_| | | |
    \_| |_/\___|_|_| |_| |_|\__,_|\__,_|_|_| Version: {}
""".format(Version)

Banner = Banner + """
          Author: Ygor Simões (f1v5)
        Github: https://github.com/f1v5
"""
