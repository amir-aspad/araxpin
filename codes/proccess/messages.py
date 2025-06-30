from colorama import init, Fore
init()


def print_error(text):
    print(Fore.RED+f'[-] {text}'+Fore.RESET)

def print_success(text):
    print(Fore.GREEN+f'[+] {text}'+Fore.RESET)
