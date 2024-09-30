import csv
import sqlite3

DATABASE = 'rolodex.db'
CSV_FILE = 'contacts.csv'  # Replace with the name of your CSV file

def get_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    return conn

def create_contacts_table():
    """Create contacts table if it doesn't exist."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def import_contacts_from_csv():
    """Read CSV file and insert contacts into the database."""
    conn = get_db()
    cursor = conn.cursor()

    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            phone = row['Phone 1 - Value']  # Adjust based on CSV column names
            if name and phone:
                cursor.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_contacts_table()
    import_contacts_from_csv()
    print("Contacts imported successfully!")
