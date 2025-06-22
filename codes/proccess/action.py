from .settings import INPUT_DIR, OUTPUT_DIR

import os


class Encrypt:
    def __init__(self, password):
        self.password = password

    def generate_input_address(self, file):
        # generate input address with only file name
        return os.path.join(INPUT_DIR, file)
    
    def generate_output_address(self, file):
        # generate output address with only file name
        return os.path.join(OUTPUT_DIR, file)

    def files(self):
        # find all file in input folder
        return os.listdir(INPUT_DIR)
    
    def read(self, file):
        # read data in file
        with open(self.generate_input_address(file), mode='r') as f:
            return f.read()
        
    def hash(self, data):
        # hash data
        return data
        
    def write(self, data, file):
        # write data in file
        with open(self.generate_output_address(file), mode='w') as f:
            f.write(self.hash(data))
            raise ValueError

    def proccess(self):
        try:
            for file in self.files():
                print(f'[+] find {file}')
                data = self.read(file)
                print(f'[+] read data in {file}')
                self.write(data, file)
                print(f'[+] write data complated')
        except:
            print(f'[!] error {file}')

    def run(self):
        print('[+] proccess started')
        self.proccess()
        print('[+] proccess down')