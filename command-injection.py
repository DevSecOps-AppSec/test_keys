import subprocess
import os

def execute_command(command):
    try:
        # Command Injection vulnerability
        output = subprocess.check_output(command, shell=True)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"

def main():
    print("Welcome to the simple command executor.")
    user_input = input("Enter the command you want to execute: ")

    # Unsafe execution of user input
    result = execute_command(user_input)
    print(f"Command output:\n{result}")

if __name__ == "__main__":
    main()
