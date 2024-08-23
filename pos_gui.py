import tkinter as tk
from tkinter import messagebox
from database import create_tables, add_food_item, remove_food_item, add_transaction, add_expense, get_daily_transactions, get_daily_expenses

class HomePOS:
    def __init__(self, root):
        self.root = root
        self.root.title("HomePOS System")
        self.create_widgets()
        create_tables()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="HomePOS System", font=("Arial", 24))
        self.label.grid(row=0, columnspan=2, pady=10)

        self.add_food_button = tk.Button(self.frame, text="Add Food Item", command=self.add_food_item)
        self.add_food_button.grid(row=1, column=0, pady=5)

        self.remove_food_button = tk.Button(self.frame, text="Remove Food Item", command=self.remove_food_item)
        self.remove_food_button.grid(row=1, column=1, pady=5)

        self.add_transaction_button = tk.Button(self.frame, text="Add Transaction", command=self.add_transaction)
        self.add_transaction_button.grid(row=2, column=0, pady=5)

        self.add_expense_button = tk.Button(self.frame, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=2, column=1, pady=5)

        self.view_transactions_button = tk.Button(self.frame, text="View Daily Transactions", command=self.view_daily_transactions)
        self.view_transactions_button.grid(row=3, column=0, pady=5)

        self.view_expenses_button = tk.Button(self.frame, text="View Daily Expenses", command=self.view_daily_expenses)
        self.view_expenses_button.grid(row=3, column=1, pady=5)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=4, columnspan=2, pady=10)

        self.cart_label = tk.Label(self.frame, text="Cart", font=("Arial", 18))
        self.cart_label.grid(row=5, columnspan=2, pady=10)

        self.cart_frame = tk.Frame(self.frame, bg="white", bd=2, relief="sunken")
        self.cart_frame.grid(row=6, columnspan=2, pady=10)

    def add_food_item(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add Food Item")

        tk.Label(self.new_window, text="Food Item Name:").grid(row=0, column=0, padx=10, pady=10)
        self.food_name_entry = tk.Entry(self.new_window)
        self.food_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.new_window, text="Food Item Price:").grid(row=1, column=0, padx=10, pady=10)
        self.food_price_entry = tk.Entry(self.new_window)
        self.food_price_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.new_window, text="Add", command=self.save_food_item).grid(row=2, columnspan=2, pady=10)

    def save_food_item(self):
        name = self.food_name_entry.get()
        try:
            price = float(self.food_price_entry.get())
            add_food_item(name, price)
            messagebox.showinfo("Success", "Food item added successfully.")
            self.new_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid price. Please enter a valid number.")

    def remove_food_item(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Remove Food Item")

        tk.Label(self.new_window, text="Food Item ID:").grid(row=0, column=0, padx=10, pady=10)
        self.food_id_entry = tk.Entry(self.new_window)
        self.food_id_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self.new_window, text="Remove", command=self.delete_food_item).grid(row=1, columnspan=2, pady=10)

    def delete_food_item(self):
        try:
            item_id = int(self.food_id_entry.get())
            remove_food_item(item_id)
            messagebox.showinfo("Success", "Food item removed successfully.")
            self.new_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid ID. Please enter a valid number.")

    def add_transaction(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add Transaction")

        tk.Label(self.new_window, text="Food Item ID:").grid(row=0, column=0, padx=10, pady=10)
        self.transaction_item_id_entry = tk.Entry(self.new_window)
        self.transaction_item_id_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.new_window, text="Quantity:").grid(row=1, column=0, padx=10, pady=10)
        self.transaction_quantity_entry = tk.Entry(self.new_window)
        self.transaction_quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.new_window, text="Add to Cart", command=self.add_to_cart).grid(row=2, columnspan=2, pady=10)

    def add_to_cart(self):
        try:
            item_id = int(self.transaction_item_id_entry.get())
            quantity = int(self.transaction_quantity_entry.get())
            self.cart.append((item_id, quantity))
            self.update_cart_display()
            self.new_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

    def update_cart_display(self):
        for widget in self.cart_frame.winfo_children():
            widget.destroy()

        for i, (item_id, quantity) in enumerate(self.cart):
            tk.Label(self.cart_frame, text=f"Item ID: {item_id}, Quantity: {quantity}").grid(row=i, column=0, padx=10, pady=5)

    def add_expense(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add Expense")

        tk.Label(self.new_window, text="Expense Description:").grid(row=0, column=0, padx=10, pady=10)
        self.expense_description_entry = tk.Entry(self.new_window)
        self.expense_description_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.new_window, text="Expense Amount:").grid(row=1, column=0, padx=10, pady=10)
        self.expense_amount_entry = tk.Entry(self.new_window)
        self.expense_amount_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.new_window, text="Add", command=self.save_expense).grid(row=2, columnspan=2, pady=10)

    def save_expense(self):
        description = self.expense_description_entry.get()
        try:
            amount = float(self.expense_amount_entry.get())
            add_expense(description, amount)
            messagebox.showinfo("Success", "Expense added successfully.")
            self.new_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")

    def view_daily_transactions(self):
        transactions = get_daily_transactions()
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Daily Transactions")

        for i, transaction in enumerate(transactions):
            tk.Label(self.new_window, text=str(transaction)).grid(row=i, column=0, padx=10, pady=5)

    def view_daily_expenses(self):
        expenses = get_daily_expenses()
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Daily Expenses")

        for i, expense in enumerate(expenses):
            tk.Label(self.new_window, text=str(expense)).grid(row=i, column=0, padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = HomePOS(root)
    root.mainloop()
