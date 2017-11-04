import pymonetdb
print("API test")
connection=pymonetdb.connect(username="monetdb",password="monetdb",hostname="127.0.0.1",database="testdb")
cursor = connection.cursor()
cursor.arraysize = 100
print(cursor.execute('SELECT * FROM ps'))
print(cursor.fetchone())
print(cursor.description)
cursor.close()
connection.close()
