import mysql.connector
import module as data


def user_interface():
    user_choice = input("\nVoulez-vous "
                        "(L)ister plantes "
                        "(A)jouter plante "
                        "(S)upprimer plante "
                        "(R)echercher plante "
                        "(Q)uitter : ").upper()
    return user_choice


def add_record(database, cursor,name_record,indication_record,used_piece_record,price_record,family_id_record):
    val = (name_record, indication_record, used_piece_record, price_record, family_id_record)
    sql = ("INSERT INTO plante (name, indication, piece_used, price, family_id) VALUES (%s, %s, %s, %s, %s)")
    cursor.execute(sql, val)
    database.commit()


def delete_record(database,cursor,user_deleted_choice):
    val = (user_deleted_choice, )
    sql = "DELETE FROM plante WHERE id = %s"
    cursor.execute(sql, val)
    database.commit()


def research_record(cursor,user_research_choice):
    val = (user_research_choice, )
    sql = ("SELECT id, name FROM plante WHERE name LIKE CONCAT('%', %s, '%')")
    cursor.execute(sql, val)
    result = cursor.fetchall()
    return result


def main(database,cursor):
    while True:
        user_choice = user_interface()
        if user_choice == "L":
            data.read_table(database)
        elif user_choice == "A":
            name_record = input("Saisissez un nom : ")
            indication_record = input("Saisissez une indication : ")
            used_piece_record = input("Saisissez la partie utilisée : ")
            price_record = input("Saisissez le prix : ")
            family_id_record = input("Saisissez l'id de la famille : ")
            add_record(database, cursor,name_record,indication_record,used_piece_record,price_record,family_id_record)
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


if __name__ == '__main__':
    database = mysql.connector.connect(user='cedric', password='Moustic26*',
                                 host='localhost',
                                 database='herborist')
    cursor = database.cursor()
    main(database, cursor)
    database.close()
