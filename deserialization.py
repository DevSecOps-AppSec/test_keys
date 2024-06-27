import pickle
import base64

def deserialize_data(serialized_data):
    try:
        # Insecure deserialization vulnerability
        data = pickle.loads(serialized_data)
        return data
    except Exception as e:
        return f"An error occurred during deserialization: {e}"

def main():
    print("Welcome to the simple deserialization service.")
    user_input = input("Enter base64-encoded serialized data: ")

    try:
        serialized_data = base64.b64decode(user_input)
        result = deserialize_data(serialized_data)
        print(f"Deserialized data:\n{result}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
