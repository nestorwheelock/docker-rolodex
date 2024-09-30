import csv
import sqlite3

DATABASE = 'rolodex.db'
CSV_FILE = 'contacts.csv'

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
            first_name = row.get('First Name', '')
            last_name = row.get('Last Name', '')
            phone = row.get('Phone 1 - Value', '')

            # Combine first and last names to form a full name
            name = f"{first_name} {last_name}".strip()

            # Only insert if both name and phone are present
            if name and phone:
                cursor.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_contacts_table()
    import_contacts_from_csv()
    print("Contacts imported successfully!")
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        first_name = row.get('First Name', '')
        last_name = row.get('Last Name', '')
        phone = row.get('Phone 1 - Value', '')

        # Combine first and last names
        name = f"{first_name} {last_name}".strip()

        # Debugging: Print out the names and phone numbers being processed
        print(f"Processing: Name: {name}, Phone: {phone}")

        # Only insert if both name and phone are present
        if name and phone:
            cursor.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
