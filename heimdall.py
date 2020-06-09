#!/usr/bin/env python3

import argparse
from datetime import datetime

from src import color as C
from src import banner as B
from src import help as Help

from lib import exploit as Exploit
from lib import update as Update

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument("-h", "--help",
                    action="store_true",
                    help="Show this help message and exit")

parser.add_argument("-u", "--url",
                    action="store",
                    type=str,
                    default=False,
                    help="Target URL (http://www.site.com/)")

parser.add_argument("-w", "--wordlist",
                    action="store",
                    type=str,
                    default="1",
                    help="Set wordlist. Default: 1 (Small) and Max: 3 (Big)")

parser.add_argument("-p", "--proxy",
                    action="store",
                    type=str,
                    default=False,
                    help="Use a proxy to connect to the target URL")

parser.add_argument("--user-agent",
                    action="store",
                    type=str,
                    default=False,
                    help="Customize the User-Agent. Default: Random User-Agent")

parser.add_argument("--update",
                    action="store_true",
                    default=False,
                    help="Upgrade Heimdall to its latest available version.")

args = parser.parse_args()

if args.update == True:
    print(B.Banner)
    print("{}[+]{} Started!  Date: {} Time: {}".format(C.GREEN, C.RESET,
                                                       datetime.now().strftime("%m/%d/%Y"), datetime.now().strftime("%H:%M")))
    Update.Upgrade()
    exit()
elif args.url == False:
    print(B.Banner)
    print(Help.Message)
    exit()
else:
    print(B.Banner)
    print("{}[+]{} Started!  Date: {} Time: {}".format(C.GREEN, C.RESET,
                                                       datetime.now().strftime("%m/%d/%Y"), datetime.now().strftime("%H:%M")))
    Exploit.Finder(args)
