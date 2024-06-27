from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

# Hardcoded encryption key (vulnerability)
key = b'0123456789abcdef'  # 16-byte key for AES

def encrypt(plaintext):
    # Weak encryption using ECB mode (vulnerability)
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_plaintext = plaintext + (16 - len(plaintext) % 16) * ' '
    ciphertext = encryptor.update(padded_plaintext.encode()) + encryptor.finalize()
    return base64.b64encode(ciphertext).decode()

def decrypt(ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(base64.b64decode(ciphertext)) + decryptor.finalize()
    return decrypted_data.decode().strip()

def main():
    print("Welcome to the insecure encryption service.")
    plaintext = input("Enter plaintext to encrypt: ")
    encrypted_text = encrypt(plaintext)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
