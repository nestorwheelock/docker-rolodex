# app.py
from flask import Flask, jsonify, request, g
import sqlite3

app = Flask(__name__)
DATABASE = 'rolodex.db'


def get_db():
    """Connect to the SQLite database."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    """Close the database connection."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/contacts', methods=['POST'])
def add_contact():
    """Add a new contact to the Rolodex."""
    data = request.json
    name = data.get('name')
    phone = data.get('phone')

    if not name or not phone:
        return jsonify({"error": "Name and phone are required"}), 400

    db = get_db()
    db.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
    db.commit()

    return jsonify({"message": "Contact added successfully"}), 201


@app.route('/contacts', methods=['GET'])
def get_contacts():
    """Get all contacts in the Rolodex."""
    db = get_db()
    cursor = db.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()

    return jsonify([{'id': row['id'], 'name': row['name'], 'phone': row['phone']} for row in contacts]), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

