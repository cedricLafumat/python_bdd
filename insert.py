import mysql.connector
db = mysql.connector.connect(user='cedric', password='Moustic26*',
                              host='localhost',
                              database='herbalist')

cursor = db.cursor()


def main():
    id_record = int(input("Saisissez l'id de votre enregistrement : "))
    name_record = input("Saisissez un nom : ")
    indication_record = input("Saisissez une indication : ")
    used_piece_record = input("Saisissez la partie utilisée : ")
    price_record = input("Saisissez le prix : ")


    cursor.execute("INSERT INTO plante (id, nom, indication, partie_utilisee, prix) VALUES ('{}','{}','{}','{}','{}')".format(id_record, name_record, indication_record, used_piece_record, price_record))
    db.commit()


if __name__ == '__main__':
    main()
