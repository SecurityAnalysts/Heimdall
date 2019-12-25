#!/usr/bin/env python3

import random

from src import color as C

Version = "BETA 2.0"
Banner = random.randrange(3)

if Banner == 0:
    Banner = """{}{}
     _   _      _               _       _ _ 
    | | | | ___(_)_ __ ___   __| | __ _| | |
    | |_| |/ _ \ | '_ ` _ \ / _` |/ _` | | |
    |  _  |  __/ | | | | | | (_| | (_| | | |
    |_| |_|\___|_|_| |_| |_|\__,_|\__,_|_|_|{} Version: {}
""".format(C.BOLD, C.YELLOW, 
           C.RESET, Version)

elif Banner == 1:
    Banner = """{}{}
                _               _       _ _ 
      /\  /\___(_)_ __ ___   __| | __ _| | |
     / /_/ / _ \ | '_ ` _ \ / _` |/ _` | | |
    / __  /  __/ | | | | | | (_| | (_| | | |
    \/ /_/ \___|_|_| |_| |_|\__,_|\__,_|_|_|{} Version: {}
""".format(C.BOLD, C.YELLOW, 
           C.RESET, Version)

elif Banner == 2:
    Banner = """{}{}
     _   _      _               _       _ _ 
    | | | |    (_)             | |     | | |
    | |_| | ___ _ _ __ ___   __| | __ _| | |
    |  _  |/ _ \ | '_ ` _ \ / _` |/ _` | | |
    | | | |  __/ | | | | | | (_| | (_| | | |
    \_| |_/\___|_|_| |_| |_|\__,_|\__,_|_|_|{} Version: {}
""".format(C.BOLD, C.YELLOW, 
           C.RESET, Version)

Banner = Banner + """{}
        Author: Ygor Simões (Security Researcher)
          Twitter: https://twitter.com/CR3DN3 
          GitHub: https://github.com/CR3DN3{}
""".format(C.CYAN, 
           C.RESET)
