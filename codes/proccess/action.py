from ..settings import INPUT_DIR, OUTPUT_DIR
from .messages import print_error, print_success

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes

import shutil
import base64
import os


class Base:
    def __init__(self, remove_state):
        self.from_ = INPUT_DIR
        self.to_ = OUTPUT_DIR
        self.remove_state = remove_state

        # create output folder for save rusult
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def generate_input_address(self, file):
        # generate input address with only file name
        return os.path.join(self.from_, file)
    
    def generate_output_address(self, file):
        # generate output address with only file name
        return os.path.join(self.to_, file)
    
    def read(self, file):
        # read data in file
        with open(self.generate_input_address(file), mode='rb') as f:
            return f.read()
        
    def files(self):
        # find all file in folder
        return os.listdir(self.from_)
    
    def proccess(self):
        try:
            for file in self.files():
                print_success(f'find {file}')
                data = self.read(file)
                print_success(f'read data from {file}')
                self.write(data, file)
                print_success('write data complated')
        except InvalidToken:
            print_error('your password is wrong. so you can not decrypt file')
        except:
            print_error(f'error {file}')
        else:
            if self.remove_state and not self.remove_input():
                print_error('have problem for remove directory')

    def run(self, password):
        self.password = self.hash_password(password)
        print_success('proccess started')
        self.proccess()
        print_success('proccess down')

    def hash_password(self, password):
        '''
        generate key with user password
        this genrate key help us to encrypt and decrypt data from input folder
        '''
        password = password.encode()
        salt = b'\xd0\x07-\x1e\xa3_\x87\xe6j`ZB\x01R\xe3~'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(password))
    
    def write(self, data, file):
        '''write data in the file'''
        with open(self.generate_output_address(file), mode='wb') as f:
            f.write(self.generate(data))

    def remove_input(self):
        '''remove input directory'''
        try:
            shutil.rmtree(INPUT_DIR)
        except:
            return False
        return True

class Encrypt(Base):
    def generate(self, data):
        '''encrypt data with user password'''
        enc = Fernet(self.password)
        return enc.encrypt(data)
        

class Decrypt(Base):
    def generate(self, data):
        '''decrypt data with user password'''
        enc = Fernet(self.password)
        return enc.decrypt(data)
        