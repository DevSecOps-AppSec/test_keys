import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

def main():
    print("Welcome to the simple file reader.")
    user_input = input("Enter the filename you want to read: ")

    # Directory Traversal vulnerability
    file_content = read_file(user_input)
    print(f"File content:\n{file_content}")

if __name__ == "__main__":
    main()
