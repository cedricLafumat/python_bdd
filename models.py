from peewee import *

db = MySQLDatabase('herborist', user='cedric', password='Moustic26*',
                                 host='localhost')

class BaseModel(Model):

    class Meta:
        database = db


class SubClass(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    name_fr = CharField(max_length=50)

    class Meta:
        table_name = "sous_classe"


class Family(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    name_fr = CharField(max_length=50)
    sous_classe = ForeignKeyField(SubClass)


class Plante(BaseModel):
    def __str__(self):
        return Plante.indication

    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    indication = CharField(max_length=70)
    piece_used = CharField(max_length=40)
    price = DecimalField(max_digits=7, decimal_places=2)
    family = ForeignKeyField(Family)
