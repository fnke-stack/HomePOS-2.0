# pos.py
from database import create_tables, add_food_item, remove_food_item, add_transaction, add_expense, get_daily_transactions, get_daily_expenses

def main():
    create_tables()
    
    while True:
        print("\nHomePOS System")
        print("1. Add Food Item")
        print("2. Remove Food Item")
        print("3. Add Transaction")
        print("4. Add Expense")
        print("5. View Daily Transactions")
        print("6. View Daily Expenses")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter food item name: ")
            price = float(input("Enter food item price: "))
            add_food_item(name, price)
            print("Food item added successfully.")
        
        elif choice == '2':
            item_id = int(input("Enter food item ID to remove: "))
            remove_food_item(item_id)
            print("Food item removed successfully.")
        
        elif choice == '3':
            item_id = int(input("Enter food item ID: "))
            quantity = int(input("Enter quantity: "))
            add_transaction(item_id, quantity)
            print("Transaction added successfully.")
        
        elif choice == '4':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(description, amount)
            print("Expense added successfully.")
        
        elif choice == '5':
            transactions = get_daily_transactions()
            print("Daily Transactions:")
            for transaction in transactions:
                print(transaction)
        
        elif choice == '6':
            expenses = get_daily_expenses()
            print("Daily Expenses:")
            for expense in expenses:
                print(expense)
        
        elif choice == '7':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
