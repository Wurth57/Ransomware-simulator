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
