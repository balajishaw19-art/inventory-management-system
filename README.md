# Inventory Management System

A simple web-based inventory management app built with Flask and SQLite.
It lets you view, add, edit, delete, search, and sort inventory items
through a clean Bootstrap interface.

## Features

- View all inventory items in a table
- Add a new item (name, quantity, price)
- Edit an existing item
- Delete an item
- Search items by name
- Sort items by name, quantity, or price
- Basic input validation (non-empty name, quantity ≥ 0, price ≥ 0)
- Friendly messages when the inventory or search results are empty

## Tech Stack

- **Python** — application logic
- **Flask** — web framework and routing
- **SQLite** — file-based database
- **HTML / Jinja2** — templates
- **Bootstrap** (via CDN) — styling

## Project Structure

```
flask-inventory-app/
├── app.py                 # Flask routes and application logic
├── db.py                  # SQLite database functions (CRUD)
├── inventory.db            # SQLite database file
├── requirements.txt        # Python dependencies
├── templates/
│   ├── inventory.html      # Main page: list, search, sort
│   ├── add.html            # Add item form
│   └── edit.html           # Edit item form
├── study.md                # Interview study notes for this project
└── README.md
```

## Setup & How to Run

1. **Clone or download this project**, then move into the project folder:
   ```
   cd flask-inventory-app
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```
   python app.py
   ```

5. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000
   ```

The database (`inventory.db`) and the `inventory` table are created
automatically the first time the app runs.
