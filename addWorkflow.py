import sqlite3

def connect_to_db():
    # Hard-coded credentials (vulnerability)
    db_user = "admin"
    db_password = "***REMOVED***"
    database = "example.db"

    conn = sqlite3.connect(database)
    return conn

def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        # Improper error handling (vulnerability)
        print(f"An error occurred: {e}")

def main():
    conn = connect_to_db()

    # SQL Injection vulnerability
    user_input = input("Enter your username: ")
    query = f"SELECT * FROM users WHERE username = '{user_input}'"

    execute_query(conn, query)
    conn.close()

if __name__ == "__main__":
    main()
