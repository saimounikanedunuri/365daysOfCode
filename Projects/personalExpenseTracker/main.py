import os
import csv
from datetime import datetime

# File to store expenses
EXPENSE_FILE = "expenses.csv"


# Load existing expenses
def load_expenses():
    expenses = []
    if not os.path.exists(EXPENSE_FILE):
        print(f"File '{EXPENSE_FILE}' not found.")
        return expenses
    with open(EXPENSE_FILE, "r") as file:
        reader = csv.reader(file)
        try:
            next(reader)  # Skip header
        except StopIteration:
            print("No header found in file.")
        expenses = [row for row in reader if row]
    return expenses


# Save a new expense
def save_expense(expense):
    file_exists = os.path.exists(EXPENSE_FILE)
    with open(EXPENSE_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            # Add header if the file is new
            writer.writerow(["Date", "Amount", "Category", "Description"])
        writer.writerow(expense)


# Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = input("Enter amount: ")
    category = input("Enter category (e.g., Food, Transport): ")
    description = input("Enter description: ")
    save_expense([date, amount, category, description])
    print("Expense added.")


# View all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nDate       | Amount | Category  | Description")
        for expense in expenses:
            print(" | ".join(expense))


# Display a monthly summary
def monthly_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    summary = {}
    for expense in expenses:
        month = datetime.strptime(expense[0], "%Y-%m-%d").strftime("%Y-%m")
        amount = float(expense[1])
        summary[month] = summary.get(month, 0) + amount
    print("\nMonthly Summary")
    for month, total in summary.items():
        print(f"{month}: ${total:.2f}")


# Main function
def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
