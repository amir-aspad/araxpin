from ..settings import INPUT_DIR, OUTPUT_DIR, PASSWORD
from .messages import print_error, print_success

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes

import hashlib
import base64
import os


class Base:
    def __init__(self):
        self.from_ = INPUT_DIR
        self.to_ = OUTPUT_DIR

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
                print_success(f'read data in {file}')
                self.write(data, file)
                print_success('write data complated')
        except InvalidToken:
            print_error('your password is wrong. so you can not decrypt file')
        except:
            print_error(f'error {file}')

    def run(self, password):
        self.password = self.hash_password(password)
        print(print_success('proccess started'))
        self.proccess()
        print(print_success('proccess down'))

    def check_password(self, password):
        hash_password = hashlib.sha3_512(password.encode())
        return hash_password.hexdigest() == PASSWORD

    def hash_password(self, password):
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
        

class Encrypt(Base):
    def hash(self, data):
        # hash data
        # return data
        enc = Fernet(self.password)
        return enc.encrypt(data)
        
    def write(self, data, file):
        # write data in file
        with open(self.generate_output_address(file), mode='wb') as f:
            f.write(self.hash(data))


class Decrypt(Base):
    def unhash(self, data):
        # unhash data
        # return data
        enc = Fernet(self.password)
        return enc.decrypt(data)
        
    def write(self, data, file):
        # write data in the file
        with open(self.generate_output_address(file), mode='wb') as f:
            f.write(self.unhash(data))

