from cryptography.fernet import Fernet

# Hardcoded key (vulnerability)
key = b'12B7pZk9bVt7i9Th9F6j6vLf-8Yk8xZmHVOS3q7eYmI='
cipher_suite = Fernet(key)

def encrypt_message(message):
    try:
        # Encrypting the message
        encrypted_text = cipher_suite.encrypt(message.encode())
        return encrypted_text
    except Exception as e:
        return f"An error occurred during encryption: {e}"

def decrypt_message(encrypted_message):
    try:
        # Decrypting the message
        decrypted_text = cipher_suite.decrypt(encrypted_message).decode()
        return decrypted_text
    except Exception as e:
        return f"An error occurred during decryption: {e}"

def main():
    print("Welcome to the insecure encryption demo.")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? ")

    if choice.lower() == 'e':
        message = input("Enter the message to encrypt: ")
        encrypted_message = encrypt_message(message)
        print(f"Encrypted message: {encrypted_message}")
    elif choice.lower() == 'd':
        encrypted_message = input("Enter the encrypted message: ").encode()
        decrypted_message = decrypt_message(encrypted_message)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please choose 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
