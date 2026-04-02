from database import connect_db

def is_duplicate(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    data = cursor.fetchone()
    conn.close()
    return data

def clean_data(name, email):
    return name.strip().title(), email.strip().lower()