from .settings import INPUT_DIR, OUTPUT_DIR
from .messages import error, success

import os


class Base:
    def __init__(self, password, action):
        self.password = password
        self.action = action
        self.from_ = INPUT_DIR if self.action=='enc' else OUTPUT_DIR
        self.to_ = OUTPUT_DIR if self.action=='enc' else INPUT_DIR

    def generate_input_address(self, file):
        # generate input address with only file name
        return os.path.join(self.from_, file)
    
    def generate_output_address(self, file):
        # generate output address with only file name
        return os.path.join(self.to_, file)
    
    def read(self, file):
        # read data in file
        with open(self.generate_input_address(file), mode='r') as f:
            return f.read()
        
    def files(self):
        # find all file in folder
        return os.listdir(self.from_)
    
    def proccess(self):
        try:
            for file in self.files():
                print(success(f'find {file}'))
                data = self.read(file)
                print(success(f'read data in {file}'))
                self.write(data, file)
                print(success('write data complated'))
        except:
            print(error(f'error {file}'))

    def run(self):
        print(success('proccess started'))
        self.proccess()
        print(success('proccess down'))


class Encrypt(Base):
    def __init__(self, password):
        super().__init__(password, 'enc')

    def hash(self, data):
        # hash data
        return data
        
    def write(self, data, file):
        # write data in file
        with open(self.generate_output_address(file), mode='w') as f:
            f.write(self.hash(data))


class Decrypt(Base):
    def __init__(self, password):
        super().__init__(password, 'dec')
        
    def unhash(self, data):
        # unhash data
        return data
        
    def write(self, data, file):
        # write data in the file
        with open(self.generate_output_address(file), mode='w') as f:
            f.write(self.unhash(data))

