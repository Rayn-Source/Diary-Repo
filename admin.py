import sqlite3
from diary import RegisterNewUser 
import pandas as pd
import sqlite3

# 1. Load your CSV
df = pd.read_csv('users.csv')

# 2. Connect to (or create) the SQLite database
conn = sqlite3.connect('my_new_database.db')

df.to_sql('imported_data', conn, if_exists='replace', index=False)

conn.close()
print("Conversion complete!")

username =""
def init_db():
    conn = sqlite3.connect('diary-repo.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(" 
                      USERNAME TEXT PRIMARY KEY UNIQUE,
                      PASSWORD TEXT,
                      FULL_NAME TEXT
                   )
                   """)
    
def addDiaryUser():
    conn = sqlite3.connect('diary-repo.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT TABLE IF NOT EXISTS users(" 
                      USERNAME TEXT PRIMARY KEY UNIQUE,
                      PASSWORD TEXT,
                      FULL_NAME TEXT
                   )
                   """)
    conn.commit()
    conn.close()

def retrieveDiaryUser():
    conn = sqlite3.connect('diary-repo.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users SET PASSWORD, FULL_NAME WHERE USERNAME=?                   )
                   """)
    conn.close()
    
def updateDiaryUser():
    conn = sqlite3.connect('diary-repo.db')
    cursor = conn.cursor()
    cursor.execute(""" UPDATE users SET PASSWORD,FULL_NAME WHERE USERNAME=?
                   """, username)
    conn.commit()
    conn.close()

def deleteDiaryUser():
    conn = sqlite3.connect('diary-repo.db')
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM users WHERE username = ?)
                   """, username)
    conn.commit()
    conn.close()
    