import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',password='Sriya@123')

if conn.is_connected():
    print('connection established')
# print(conn)

mycursor = conn.cursor()
mycursor.execute('create database pythondb')
print(mycursor)