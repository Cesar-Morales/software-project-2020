""" 
Modelo de user

Se crea tanto el modelo del user que se va a relacionar con la tabla 
de la base de datos como la misma tabla.

Además se definen los metodos para realizar los cinco métodos del modulo
"""

from app import db, login_manager
from sqlalchemy import or_
from app.models.usuario_tiene_rol import usuario_tiene_rol
from flask_login import UserMixin
from app.models.rol import Rol
from flask_sqlalchemy import SQLAlchemy
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter_by(id=user_id).first()

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    active = db.Column(db.Boolean, default=True)

    roles = db.relationship('Rol', secondary=usuario_tiene_rol, back_populates='users')

    def create(requestform):
         username = requestform.get("username")
         email = requestform.get("email")
         last_name = requestform.get("last_name")
         first_name = requestform.get("first_name")
         password = requestform.get("password")
         #Verificamos si el nombre de usuario o email ya estan en uso
         user = db.session.query(User).filter(or_(User.username == username , User.email == email)).first()
         if  user: 
             return False
         else:     
            nuevo = User(email=email, last_name=last_name, first_name=first_name, password=password,username=username)
            roles = db.session.query(Rol).filter_by(name="user").first()
            nuevo.roles.append(roles)
            db.session.add(nuevo)
            db.session.commit() 
            return True  

    #Funcion de busqueda de usuarios
    #inicialmente busco por nombre de usuario que es unico, luego voy a buscar por activo o bloqueado, que trae mas resultados
    #pero esto una vez que este lista la tabla de usuarios con los campos necesarios
    def search(requestform):
         usernam = requestform.get("search")
         actdeact = requestform.get("active")
         #Si no ingresan string a buscar, traigo todos los usuarios, verificando si mandaron activos o bloqueados.
         if not usernam:
             users = db.session.query(User).filter(User.active == actdeact).all()
         else: 
             users = db.session.query(User).filter(User.username.like('%'+usernam+'%'),User.active == actdeact).all()
         return users

    def block(requestForm):
        idUser = requestForm.get("bloquear")
        user = db.session.query(User).filter(User.id == idUser).first()
        user.active = 0 
        db.session.commit()
        return  True
        
    def activate(requestForm):
        idd = requestForm.get("activar")
        user = db.session.query(User).filter(User.id == idd).first()
        user.active = 1 
        db.session.commit()
        return  True

