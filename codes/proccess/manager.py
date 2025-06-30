from .text import description, syng
from .action import Encrypt, Decrypt
from .messages import print_error

from os import system, name


def run():
    print(description)
    while True:
        cmd = input(syng).lower().strip()

        if cmd == 'enc':
            password = input('your password ? ')
            enc = Encrypt()
            if password and enc.check_password(password):
                enc_password = input('write your encrypt password : ').strip()
                enc.run(enc_password)
            else:
                print_error('password have problem')

        elif cmd == 'dec':
            password = input('your password ? ')
            dec = Decrypt()
            if password and dec.check_password(password):
                dec_password = input('write your decrypt password : ').strip()
                dec.run(dec_password)
            else:
                print_error('password have problem')
        
        elif cmd == 'cls':
            system('cls' if name == 'nt' else 'clear')
        
        elif cmd == 'exit':
            if input('are you sure (y/n) ? ').lower() == 'y':break

        elif cmd == 'help':
            print(description)