import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Root@123'
)

cursorObject= dataBase.cursor()

cursorObject.execute("CREATE DATABASE dcrmdb")

print("DB created")