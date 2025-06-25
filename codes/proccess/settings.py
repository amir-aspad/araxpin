from dotenv import load_dotenv
import os
load_dotenv()


BASE_DIR = os.getcwd()

INPUT_DIR = os.path.join(BASE_DIR, 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

PASSWORD = os.getenv('PASSWORD')
