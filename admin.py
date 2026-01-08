import sqlite3
from diary import RegisterNewUser 

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
    