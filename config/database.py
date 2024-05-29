import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base #manipular todas la tablas

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__)) #Leer el directorio actual del archivo
database_url = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'#join para unri las 2 url

#Motor de la base de datos

engine = create_engine(database_url, echo=True)

#Session para conectarse a la base de datos
Session = sessionmaker(bind=engine)
Base = declarative_base()