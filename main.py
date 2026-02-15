from models import Expense
from database import init_db
from database import add_expense
from database import get_all_expenses

def main():
    
    init_db()
    
    
    print("\n--- Saving Data ---")
    try:
        # 1. Create the object using our model
        lunch = Expense(amount=12.50, category="Food", description="Sandwich at Efrei")
        
        # 2. Save it to the database
        add_expense(lunch.amount, lunch.category, lunch.description, lunch.date)
        
    except ValueError as e:
        print(f"Error: {e}")

    print("\n--- Reading Data ---")
    # 3. Read it back from the database
    saved_data = get_all_expenses()
    
    for row in saved_data:
        print(row)

if __name__ == "__main__":
    main()