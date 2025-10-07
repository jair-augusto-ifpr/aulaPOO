from peewee import *

db = SqliteDatabase('escola.db')

class BaseModel(Model):
    class Meta:
        database = db

def criar_tabelas():
    from Aluno import Aluno
    from Professor import Professor
    from SalaAula import SalaAula, SalaAluno

    db.connect()
    db.create_tables([Professor, Aluno, SalaAula, SalaAluno])
    db.close()
