import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',password='Sriya@123',database='pythondb')

mycursor = conn.cursor()

sql = 'insert into student (name,branch,id) values(%s,%s,%s)'
#val = ('john','cse',56)

# if user want to create multiple value then you can creat list 
val = [('john','cse','56'),('mike','IT','78'),('tyson','me','80')]
#mycursor.execute(sql,val)
mycursor.executemany(sql,val)
conn.commit()
print(mycursor.rowcount,'record inserted')