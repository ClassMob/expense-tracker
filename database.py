import sqlite3

DB_NAME = "expenses.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    
    cursor = conn.cursor()
    
    sql_query = """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        date TEXT NOT NULL
    );
    """
    
    cursor.execute(sql_query)
    conn.commit()
    conn.close()
    
    print("Database initialized successfully")
    
    
def add_expense(amount: float, category: str, description:str, date:str):
    """Insert new data in the database"""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        
        sql_query = """
        INSERT INTO expenses(amount, category, description, date) VALUES (?, ?, ?, ?)
        """
        
        cursor.execute(sql_query, (amount, category, description, date))
        conn.commit()
        print(f"Saved: {category} - {amount}€")
        

def get_all_expenses():
    """fetches all expenses from the database"""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor();
        cursor.execute("SELECT * FROM expenses") 
        
        records = cursor.fetchall()
        return records