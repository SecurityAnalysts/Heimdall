# ⚡️ Heimdall ⚡️
![Screenshot](https://raw.githubusercontent.com/f1v5/Heimdall/master/doc/images/heimdall.gif)


## What is this?

Heimdall is a project created entirely in Python to facilitate the intrusion testing process on a website. Simple, powerful, fast and easy to use code can use. It uses the brute force method to find the administrator directory of a target site.

## Screenshot

![Screenshot](https://raw.githubusercontent.com/f1v5/Heimdall/master/doc/images/heimdall_screenshot.png)

## Tested on

* macOS Catalina
* Kali Linux

## Installation

You can download the latest tarball by clicking [here](https://github.com/f1v5/Heimdall/tarball/master) or latest zipball by clicking [here](https://github.com/f1v5/Heimdall/zipball/master).

```
$ git clone --depth 1 https://github.com/f1v5/Heimdall.git
$ cd Heimdall && pip3 install -r requirements.txt
```

## Usage

```
Usage: ./heimdall.py [-h, --help] [-u, --url] [--wordlist (1, 2, 3)]
                     [--user-agent <custom>] [--update]

Description: Heimdall is a project created entirely in Python to facilitate the 
             intrusion testing process on a website. Simple, powerful, fast and 
             easy to use code can use. It uses the brute force method to find 
             the administrator directory of a target site.

Optional Arguments:

   -h, --help             Show this help message and exit
   -u URL, --url URL      Target URL (http://www.site.com/)
   --wordlist (1, 2, 3)   Set wordlist. Default: 1 (Small) and Max: 3 (Big)
   --user-agent           Customize the User-Agent. Default: Random User-Agent
   --update               Upgrade Heimdall to its latest available version.
```

### Examples

```
./heimdall.py --url www.target.com --wordlist 1
./heimdall.py --url www.target.com --wordlist 2 --user-agent <USER-AGENT>
./heimdall.py --url www.target.com --wordlist extra/wordlists/custom.txt
./heimdall.py --update
```

## Translations

* [English](https://github.com/f1v5/Heimdall/blob/master/README.md)
* [Portuguese](https://github.com/f1v5/Heimdall/blob/master/doc/translations/README-pt-BR.md)