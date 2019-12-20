# Heimdall
![Screenshot](https://raw.githubusercontent.com/f1v5/Heimdall/master/doc/images/heimdall.gif)


## O que é isso?

Heimdall é um projeto criado inteiramente em Python para facilitar o processo de teste de intrusão em um site. Um código simples, poderoso, rápido e fácil de usar pode usar. Ele utiliza o método de força bruta para encontrar o diretório de administrador de um site alvo.

## Screenshot

![Screenshot](https://raw.githubusercontent.com/f1v5/Heimdall/master/doc/images/heimdall_screenshot.png)

## Instalação

Você pode baixar o tarball mais recente clicando [aqui](https://github.com/f1v5/Heimdall/tarball/master) ou zipball mais recente, clicando [aqui](https://github.com/f1v5/Heimdall/zipball/master).

```
$ git clone --depth 1 https://github.com/f1v5/Heimdall.git
$ cd Heimdall && pip3 install -r requirements.txt
```

## Uso

```
Usage: ./heimdall.py [-h, --help] [-u, --url] [--wordlist (1, 2, 3)]
                   [--user-agent <custom>]

Description: Fast, simple, powerful and didactic this admin finder 
             written entirely in Python3.

Optional Arguments:

   -h, --help             Show this help message and exit
   -u URL, --url URL      Target URL (http://www.site.com/)
   --wordlist (1, 2, 3)   Set wordlist. Default: 1 (Small) and Max: 3 (Big)
   --user-agent           Customize the User-Agent. Default: Random User-Agent
```

### Exemplos

```
./heimdall.py --url www.target.com --wordlist 1
./heimdall.py --url www.target.com --wordlist 2 --user-agent <USER-AGENT>
./heimdall.py --url www.target.com --wordlist extra/wordlists/custom.txt
```

## Translations

* [English](https://github.com/f1v5/Heimdall/README.md)
* [Portuguese](https://github.com/f1v5/Heimdall/doc/translations/README-pt-BR)
