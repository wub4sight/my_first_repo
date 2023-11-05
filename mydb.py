import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'benb00tSTr@P43'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")