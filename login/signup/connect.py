import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conn = mysql.connector.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        database=os.getenv("database"),
        password=os.getenv("password")
        
    )
    print("Successfully connected")
    
    cursor = conn.cursor(buffered=True)
    
    user = input("Enter your Username: ")
    password = input("Enter you Password: ")
    
    cursor.execute(
    "select username from users where username = %s", (user,)
    )
    result = cursor.fetchone()
    
    if result:
        print("User exist")

    
    cursor.execute(
    "INSERT INTO users (username, password) VALUES (%s, %s)",
    (user, password)
    
    )
    
    conn.commit()
    
    

    
  

except mysql.connector.Error as error:
    print("DB connection failed")
    print(error)