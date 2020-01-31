import mysql.connector




def read_table(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM plante")

    result = cursor.fetchall()

    for record in result:
        print(record)

    # db.close()


if __name__ == '__main__':
    db = mysql.connector.connect(user='cedric', password='Moustic26*',
                                 host='localhost',
                                 database='herbalist')
    read_table(db)
    db.close()

# read_table()

