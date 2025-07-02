# 🛡️ araxpin

**araxpin** is a simple yet powerful Python tool for encrypting and decrypting files using a passphrase. It works offline, supports all file types, and preserves folder structures from input to output.

## 🚀 Features

- 🔐 Two-way encryption & decryption with a user-defined password
- 📁 Drag-and-drop files into the `input/` folder — get results in `output/`
- 🗂️ Automatically keeps folder structure from `input/` to `output/`
- ⚙️ Works with any file format (PDF, DOCX, ZIP, images, code files, etc.)
- 🧠 Minimal, clean CLI — no prior experience needed
- 🌐 100% offline and secure

## 📁 Project Structure

```
araxpin/
├── input/              # Files/folders to encrypt or decrypt
├── output/             # Encrypted or decrypted files, preserving structure
├── run.py              # Main program
├── requirements.txt    # Required Python packages
└── README.md           # Project documentation
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
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## 🔒 Security Notes

- ✅ Your files never leave your machine — fully offline.
- ❗ Don’t forget your password. There is no recovery option.
- 🔐 The same password must be used to decrypt files.
