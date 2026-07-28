# db.py
# This file handles everything related to our SQLite database.
# Every function here follows the same pattern:
# 1. Open a connection to the database file
# 2. Create a cursor (used to run SQL commands)
# 3. Run the SQL query
# 4. Commit the change (only needed for INSERT/UPDATE/DELETE)
# 5. Close the connection

import sqlite3

DB_NAME = "inventory.db"


def init_db():
    """Create the inventory table if it does not already exist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')

    connection.commit()
    connection.close()


def get_all_items():
    """Return every row from the inventory table as a list of tuples."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()

    connection.close()
    return items


def add_item(name, quantity, price):
    """Insert a new item into the inventory table."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # The ? placeholders keep this query safe from SQL injection.
    cursor.execute(
        "INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)",
        (name, quantity, price)
    )

    connection.commit()
    connection.close()


def delete_item(item_id):
    """Delete a single item from the inventory table using its ID."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))

    connection.commit()
    connection.close()


def get_item_by_id(item_id):
    """Return a single item (as a tuple) matching the given ID, or None."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM inventory WHERE id = ?", (item_id,))
    item = cursor.fetchone()

    connection.close()
    return item


def update_item(item_id, name, quantity, price):
    """Update the name, quantity and price of an existing item."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE inventory SET name = ?, quantity = ?, price = ? WHERE id = ?",
        (name, quantity, price, item_id)
    )

    connection.commit()
    connection.close()


# Running "python db.py" directly will just create the database and table.
if __name__ == "__main__":
    init_db()
    print("Database initialized.")
