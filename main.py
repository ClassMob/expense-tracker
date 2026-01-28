from models import Expense
from database import init_db

def main():
    
    init_db()
    
    
    try :
        lunch = Expense(amount=12.5, category="Food", description="Sandwitch at Efrei")
        print(f"Success ! Created expense : {lunch}")
    except ValueError as e:
            print(f"Error: {e}")
    
if __name__ == "__main__":
    main()