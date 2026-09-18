import mysql.connector
import os
from dotenv import load_dotenv
import pwinput
import bcrypt

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
    
    if len(password) < 8:
        print("Password must be 8 character")
        exit()
    
    cursor.execute(
    "select username from users where username = %s", (user,)
    )
    result = cursor.fetchone()
    
    if result:
        print("User exist")
        exit()

    hashed_password = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
    )
    
    
    cursor.execute(
    "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
    (user, hashed_password.decode("utf-8"), email)
    
    )
    print("Account successfully created!")
    
    conn.commit()
    cursor.close()
    conn.close()
    
    

except mysql.connector.Error as error:
    print("DB connection failed")
    print(error)