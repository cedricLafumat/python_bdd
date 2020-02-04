from models import *


def average_price_by_indication():
    plantes = Plante.select(fn.AVG(Plante.price),Plante.indication).order_by(Plante.indication).group_by(Plante.indication)
    for plante in plantes:
        print(plante)


if __name__ == '__main__':
    average_price_by_indication()
