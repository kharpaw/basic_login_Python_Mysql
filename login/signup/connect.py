import mysql.connector
import os
from dotenv import load_dotenv
import pwinput

load_dotenv()

try:
    conn = mysql.connector.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        database=os.getenv("database"),
        password=os.getenv("password")
        
    )

    
    cursor = conn.cursor(buffered=True)
    
    print("*****CREATE YOU ACCOUNT*****")
    
    email = input("Enter you email: ")
    user = input("Enter your Username: ")
    password = pwinput.pwinput("Enter you Password: ")
    

    
    cursor.execute(
    "select username from users where username = %s", (user,)
    )
    result = cursor.fetchone()
    
    if result:
        print("User exist")
        exit()

    
    cursor.execute(
    "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
    (user, password, email)
    
    )
    print("Account successfully created!")
    
    conn.commit()
    
    

    
  

except mysql.connector.Error as error:
    print("DB connection failed")
    print(error)