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