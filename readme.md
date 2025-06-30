# 🛡️ araxpin

**araxpin** is a Python-based tool designed for two-way encryption and decryption of files using a user-defined passphrase. It works with all file types and is structured around two key folders: `input/` and `output/`.

## 🚀 Features

- 🔐 Encrypt and decrypt using the same password.
- 📁 File-based workflow: drag files into `input/`, get results in `output/`.
- 📦 Supports any file format.
- 💡 Simple and intuitive command-line interface.

## 📁 Folder Structure

```
araxpin/
├── input/          # Place files here to be encrypted or decrypted
├── output/         # Results will be saved here
├── run.py          # Core script
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

1. Put your file(s) into the `input/` directory.
2. Run the script using the command below.
3. Enter a passphrase when prompted.
4. Processed files will appear in the `output/` folder.

> 💡 To decrypt, simply move the encrypted files to `input/` and use the same password. Decrypted files will be restored to `output/`.

## 🖥️ Run the Program

Copy and paste this into your terminal to run the script:

```bash
git clone git@github.com:amir-aspad/araxpin.git
cd araxpin
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## 🔒 Important Notes

- Remember your passphrase — losing it means losing access to your files.
- Encrypted output depends on both the file content and password for maximum security.
