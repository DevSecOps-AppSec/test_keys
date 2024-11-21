from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os

# Function to encrypt data
def encrypt_aes_gcm(key, plaintext, associated_data):
    # Generate a random 96-bit nonce
    nonce = os.urandom(12)

    # Create AES-GCM cipher
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()

    # Attach associated data (optional, for authenticity)
    if associated_data:
        encryptor.authenticate_additional_data(associated_data)

    # Encrypt the plaintext
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return nonce, ciphertext, encryptor.tag

# Function to decrypt data
def decrypt_aes_gcm(key, nonce, ciphertext, tag, associated_data):
    # Create AES-GCM cipher
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()

    # Attach associated data (optional, for authenticity)
    if associated_data:
        decryptor.authenticate_additional_data(associated_data)

    # Decrypt the ciphertext
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext

# Main function to test the encryption and decryption
if __name__ == "__main__":
    # Key (must be 16, 24, or 32 bytes long for AES)
    key = os.urandom(32)  # 256-bit key

    # Plaintext
    plaintext = b"Sensitive data to encrypt"

    # Associated data (optional, e.g., metadata)
    associated_data = b"authenticated but not encrypted"

    print("Original Plaintext:", plaintext)

    # Encrypt the plaintext
    nonce, ciphertext, tag = encrypt_aes_gcm(key, plaintext, associated_data)

    print("Ciphertext (hex):", ciphertext.hex())
    print("Nonce (hex):", nonce.hex())
    print("Authentication Tag (hex):", tag.hex())

    # Decrypt the ciphertext
    try:
        decrypted_plaintext = decrypt_aes_gcm(key, nonce, ciphertext, tag, associated_data)
        print("Decrypted Plaintext:", decrypted_plaintext)
    except Exception as e:
        print("Decryption failed:", str(e))
      
