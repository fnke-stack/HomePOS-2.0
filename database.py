import sqlite3

def create_tables():
    conn = sqlite3.connect('pos.db')
    cursor = conn.cursor()
    # Existing code for creating other tables
    conn.commit()
    conn.close()

def add_food_item(name, price):
    conn = sqlite3.connect('pos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO food_items (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()

def remove_food_item(item_id):
    conn = sqlite3.connect('pos.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM food_items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

def add_transaction(item_id, quantity):
    conn = sqlite3.connect('pos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (item_id, quantity) VALUES (?, ?)", (item_id, quantity))
    conn.commit()
    conn.close()

def add_expense(description, amount):
    conn = sqlite3.connect('pos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (description, amount) VALUES (?, ?)", (description, amount))
    conn.commit()
    conn.close()

def get_daily_transactions():
    conn = sqlite3.connect('pos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE date = date('now')")
    transactions = cursor.fetchall()
    conn.close()
    return transactions

def get_daily_expenses():
    conn = sqlite3.connect('pos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE date = date('now')")
    expenses = cursor.fetchall()
    conn.close()
    return expenses
