import mysql.connector
import read as data


def user_interface():
    user_choice = input("\nVoulez-vous "
                        "(L)ister plantes "
                        "(A)jouter plante "
                        "(S)upprimer plante "
                        "(R)echercher plante "
                        "(Q)uitter : ").upper()
    return user_choice


def add_record(database, cursor,id_record,name_record,indication_record,used_piece_record,price_record):
    # id_record = int(input("Saisissez l'id de votre enregistrement : "))
    # name_record = input("Saisissez un nom : ")
    # indication_record = input("Saisissez une indication : ")
    # used_piece_record = input("Saisissez la partie utilisée : ")
    # price_record = input("Saisissez le prix : ")

    cursor.execute(
        "INSERT INTO plante (id, nom, indication, partie_utilisee, prix) VALUES ('{}','{}','{}','{}','{}')".format(
            id_record, name_record, indication_record, used_piece_record, price_record))
    database.commit()


def delete_record(database,cursor,user_deleted_choice):
    cursor.execute(
        "DELETE FROM plante WHERE id = {}".format(user_deleted_choice))
    database.commit()


def research_record(cursor,user_research_choice):
    cursor.execute(
        "SELECT * FROM plante WHERE nom LIKE ('%{}%')".format(user_research_choice))
    result = cursor.fetchall()
    return result


def main(database,cursor):
    while True:
        user_choice = user_interface()
        if user_choice == "L":
            data.read_table(database)
        elif user_choice == "A":
            id_record = int(input("Saisissez l'id de votre enregistrement : "))
            name_record = input("Saisissez un nom : ")
            indication_record = input("Saisissez une indication : ")
            used_piece_record = input("Saisissez la partie utilisée : ")
            price_record = input("Saisissez le prix : ")
            add_record(database, cursor,id_record,name_record,indication_record,used_piece_record,price_record)
        elif user_choice == "S":
            data.read_table(database)
            user_deleted_choice = int(input("\nSaisissez l'id de la plante à supprimer : "))
            delete_record(database, cursor, user_deleted_choice)
        elif user_choice == "R":
            user_research_choice = input("\nSaisissez le nom de la plante recherchée : ")
            result = research_record(cursor,user_research_choice)
            print(result)
        elif user_choice == "Q":
            break


    # cursor.execute("UPDATE plante SET partie_utilisee = 'feuilles';")
    # database.commit()
    #
    # cursor.execute('INSERT INTO plante(id, nom, indication, partie_utilisee, prix) VALUES '
    #                '(1, "Menthe poivrée", "Anesthésiant", "feuiles", 3),'
    #                '(2, "Absinthe", "Antiseptique", "feuiles", 4),'
    #                '(3, "Ail", "Antiseptique", "feuiles", 1),'
    #                '(4, "Basilic", "Antiseptique", "feuiles", 5),'
    #                '(5, "Carotte", "Digestion", "feuiles", 2.2),'
    #                '(6, "Aigremoine", "Digestion", "feuiles", 5.4),'
    #                '(7, "Ronce", "Digestion", "feuiles", 3.21),'
    #                '(8, "Linaire commune", "Diurétique", "feuiles", 1.12),'
    #                '(9, "Mélilot officinal", "Diurétique", "feuiles", 13.22);')
    #
    # database.commit()

if __name__ == '__main__':
    database = mysql.connector.connect(user='cedric', password='Moustic26*',
                                 host='localhost',
                                 database='herbalist')
    cursor = database.cursor()
    main(database, cursor)
    database.close()
