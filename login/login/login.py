import mysql.connector
from dotenv import load_dotenv
import os
import pwinput
load_dotenv()

try:
    conn = mysql.connector.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database")
    )
    
    print("*****LOGIN*****")
    user = input("Enter you username: ")
    password = pwinput.pwinput("Enter your password: ")
    
    cursor = conn.cursor()
    cursor.execute(
    "select * from users where username = %s and password =  %s ", (user, password,) )
    
    result = cursor.fetchone()
    
    if result:
        print("You are successfully Login")
    else:
        print("Access denied")
except mysql.connector.Error as error:
    print("DB connection failed")
    print(error)
    
