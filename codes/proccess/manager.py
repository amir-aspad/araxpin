from .text import description, syng
from .action import Encrypt, Decrypt
from .messages import print_error

from os import system, name


def run():
    print(description)
    while True:
        cmd = input(syng).lower().strip()

        if cmd == 'enc' or cmd == 'dec':
            password = input('your password ? ')

            remove_input_text = 'remove input file after proccess down (y or n) ?'
            remove_input_state = True if input(remove_input_text).lower().strip() == 'y' else False

            if password:
                if cmd == 'enc':
                    instance = Encrypt(remove_input_state)
                else:
                    instance = Decrypt(remove_input_state)
                instance.run(password)
            else:
                print_error('password have problem')
        
        elif cmd == 'cls':
            system('cls' if name == 'nt' else 'clear')
        
        elif cmd == 'exit':
            if input('are you sure (y/n) ? ').lower() == 'y':break

        elif cmd == 'help':
            print(description)