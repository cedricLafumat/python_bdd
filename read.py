import mysql.connector
db = mysql.connector.connect(user='cedric', password='Moustic26*',
                              host='localhost',
                              database='herbalist')

cursor = db.cursor()

cursor.execute("SELECT * FROM plante")

result = cursor.fetchall()

for record in result:
    print(record)