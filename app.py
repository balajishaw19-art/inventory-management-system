# app.py
# Main Flask application. This file defines the routes (URLs) of our
# inventory management app and connects them to the functions in db.py.

from flask import Flask, render_template, request, redirect, url_for, abort
import db

app = Flask(__name__)

# Make sure the database and table exist before the app starts handling requests.
db.init_db()


@app.route('/')
def home():
    """Show all inventory items. Supports optional search and sort via query params."""
    search = request.args.get('search', '')   # e.g. /?search=shirt
    sort_by = request.args.get('sort', '')     # e.g. /?sort=name

    items = db.get_all_items()

    # --- Search: keep only items whose name contains the search text ---
    if search:
        items = [item for item in items if search.lower() in item[1].lower()]

    # --- Sort: item is a tuple (id, name, quantity, price) ---
    if sort_by == 'name':
        items = sorted(items, key=lambda item: item[1].lower())
    elif sort_by == 'quantity':
        items = sorted(items, key=lambda item: item[2])
    elif sort_by == 'price':
        items = sorted(items, key=lambda item: item[3])

    return render_template('inventory.html', items=items, search=search)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Show the add-item form (GET) or handle the form submission (POST)."""
    error = ''

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        quantity = request.form.get('quantity', '')
        price = request.form.get('price', '')

        # Basic validation: name must not be empty, quantity/price must not be empty
        if not name or not quantity or not price:
            error = 'Please enter valid values. Name, quantity and price are required.'
        else:
            quantity = int(quantity)
            price = float(price)

            # Basic validation: quantity and price cannot be negative
            if quantity < 0 or price < 0:
                error = 'Quantity and price cannot be negative.'
            else:
                db.add_item(name, quantity, price)
                return redirect(url_for('home'))

    return render_template('add.html', error=error)


@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    """Delete an item by ID and go back to the home page."""
    db.delete_item(item_id)
    return redirect(url_for('home'))


@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    """Show the edit form pre-filled with item details (GET) or save changes (POST)."""
    item = db.get_item_by_id(item_id)
    if item is None:
        abort(404)
    error = ''

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        quantity = request.form.get('quantity', '')
        price = request.form.get('price', '')

        if not name or not quantity or not price:
            error = 'Please enter valid values. Name, quantity and price are required.'
        else:
            quantity = int(quantity)
            price = float(price)

            if quantity < 0 or price < 0:
                error = 'Quantity and price cannot be negative.'
            else:
                db.update_item(item_id, name, quantity, price)
                return redirect(url_for('home'))

    return render_template('edit.html', item=item, error=error)


if __name__ == '__main__':
    app.run(debug=True)
