import mysql.connector

my_database = mysql.connector.connect(
    host="localhost", user="python_kurs", passwd="password1234"
)

cursor = my_database.cursor()
# cursor.execute("CREATE DATABASE my_users")

cursor.execute("SHOW DATABASES")
for database in cursor:
    print(database)
