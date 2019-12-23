#!/usr/bin/env python3

import os

from src import color as C

def Upgrade():
    print("{}[+]{} Updating Heimdall.\n".format(C.GREEN, C.RESET))
    try:
        os.system("git reset --hard && git pull")
        print("\n{}[+]{} Heimdall was successfully updated.".format(C.GREEN, C.RESET))
    except Exception:
        print("\n{}[!]{} Couldn't retrieve update.".format(C.RED, C.RESET))
        print("{}[!]{} Please download the latest version from https://github.com/f1v5/Heimdall".format(C.RED, C.RESET))