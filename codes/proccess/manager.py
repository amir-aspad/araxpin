from .messages import description, syng

from os import system, name


def run():
    print(description)
    while True:
        cmd = input(syng).lower().strip()

        if cmd == 'enc':
            pass

        elif cmd == 'dec':
            pass
        
        elif cmd == 'cls':
            system('cls' if name == 'nt' else 'clear')
        
        elif cmd == 'exit':
            if input('are you sure (y/n) ? ').lower() == 'y':break

        elif cmd == 'help':
            print(description)