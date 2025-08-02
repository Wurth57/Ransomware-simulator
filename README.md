# 🛡️ Ransomware Simulator (Educational Use Only)

This project is a **safe and controlled ransomware simulation** script developed in Python.  
Its goal is to help educate users on the potential impact of ransomware attacks by allowing them to experience a simulated attack in a non-destructive environment.

---

## 🚀 Features

- 🔐 Encrypts `.txt` files in the same folder using Fernet symmetric encryption
- 📌 Automatically generates and loads a secure encryption key (`key.key`)
- 🧨 Displays a ransomware-style popup message (Windows only)
- 🖼️ Changes the desktop wallpaper to a warning image
- 🧭 Interactive menu with user options

---

## ⚙️ Requirements

- Python 3.6+
- Windows OS (for popup and wallpaper features)

### Install dependencies

```bash
pip install cryptography

How to Use
Clone or download this repository

Place .txt files in the same folder as lab8_ransom.py

Run the script:

bash
Copiar
Editar
python lab8_ransom.py
Choose one of the menu options:

1 - Encrypt .txt files

2 - Show ransomware popup and wallpaper

3 - Full ransomware simulation (encrypt + visual)

4 - Exit

📌 Notes
The script does not rename or delete files, and encryption can be reversed manually with the same key.

All encryption is done locally, and no data is sent externally.

The simulation is meant for training and awareness only — not for malicious purposes.

⚠️ Disclaimer
This tool is intended strictly for educational and training purposes.
Misuse of this code is your own responsibility. Do not use it to harm or threaten others.

👨‍💻 Author
Diogo (Wurth57)
Security enthusiast | Educational projects | Defender mindset

yaml
Copiar
Editar

---

### ✅ Para adicionares ao repositório:

1. Cria um novo ficheiro `README.md` na pasta do projeto.
2. Cola o conteúdo acima e guarda.
3. No terminal:

```bash
git add README.md
git commit -m "Add English README with full project overview"
git push
