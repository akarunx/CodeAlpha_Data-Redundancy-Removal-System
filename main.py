from database import create_table, connect_db
from utils import is_duplicate, clean_data

create_table()

def add_user():
    name = input("Enter name: ")
    email = input("Enter email: ")

    name, email = clean_data(name, email)

    if is_duplicate(email):
        print("Duplicate data found. Entry not added.")
    else:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()
        print("Unique data added successfully.")

def view_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    print("\nStored Data:")
    if not rows:
        print("No data found.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]}")

def delete_user():
    user_id = input("Enter user ID to delete: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("User deleted (if ID exists).")

while True:
    print("\n===== Data Redundancy Removal System =====")
    print("1. Add User")
    print("2. View Users")
    print("3. Delete User")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        view_users()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice")