#!/usr/bin/env python3

Message = """
Usage: ./heimdall.py [-h, --help] [-u, --url] [--wordlist (1, 2, 3)]
                   [--user-agent <custom>]

Description: Heimdall is a project created entirely in Python to facilitate the 
             intrusion testing process on a website. Simple, powerful, fast and 
             easy to use code can use. It uses the brute force method to find 
             the administrator directory of a target site.

Optional Arguments:

   -h, --help             Show this help message and exit
   -u URL, --url URL      Target URL (http://www.site.com/)
   --wordlist (1, 2, 3)   Set wordlist. Default: 1 (Small) and Max: 3 (Big)
   --user-agent           Customize the User-Agent. Default: Random User-Agent
"""