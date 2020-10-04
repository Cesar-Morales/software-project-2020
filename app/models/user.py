from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from app import db

class User(db.Model):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, unique=True, nullable=False)
    first_name = Column(String, unique=True, nullable=False)
    last_name = Column(String, unique=True, nullable=False)

    def create(requestform):
         username = requestform.get("username")
         email = requestform.get("email")
         last_name = requestform.get("last_name")
         first_name = requestform.get("first_name")
         password = requestform.get("password")
        
         nuevo = User(email=email, last_name=last_name, first_name=first_name, password=password)
         db.add(nuevo)
         db.commit()   
