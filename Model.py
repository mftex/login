from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = 'root'
SENHA = 'asdasds'
HOST = 'localhost'
BANCO = 'login'
PORTA = '3306'

CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Classe usuário que abarcará os métodos de cadastro e login descritos na Controller
class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(length=50))
    email = Column(String(length=200))
    senha = Column(String(length=100))

Base.metadata.create_all(engine)