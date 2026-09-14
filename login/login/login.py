import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

try:
    conn = mysql.connector.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database")
    )
    print("DB successfully connected")
    
    user = input("Gimme you USERNAME: ")
    password = input("Gimme you PASSWORD: ")
    
    cursor = conn.cursor()
    cursor.execute(
    "select * from users where username = %s and password =  %s ", (user, password,) )
    
    result = cursor.fetchone()
    
    if result:
        print("You are successfully Login, Welcome")
    else:
        print("Access denied")
except mysql.connector.Error as error:
    print("DB connection failed")
    print(error)
    
