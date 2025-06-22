from colorama import init, Fore
init()


def error(text):
    return Fore.RED+f'[-] {text}'+Fore.RESET

def success(text):
    return Fore.GREEN+f'[+] {text}'+Fore.RESET
