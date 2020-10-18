""" 
Modelo de user

Se crea tanto el modelo del user que se va a relacionar con la tabla 
de la base de datos como la misma tabla.

Además se definen los metodos para realizar los cinco métodos del modulo
"""
from flask.json import JSONEncoder
from flask import jsonify
from app import db, login_manager
from sqlalchemy import or_
from app.models.usuario_tiene_rol import usuario_tiene_rol
from flask import current_app
from flask_login import UserMixin
from werkzeug.utils import secure_filename
from app.models.rol import Rol
from flask_sqlalchemy import SQLAlchemy
import json
import os
from app.helpers.forms import UserForm
from flask import session
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
    deleted = db.Column(db.Boolean, default=False)
    image_name = db.Column(db.String(300), default='')
    roles = db.relationship('Rol', secondary=usuario_tiene_rol, back_populates='users')

    def create(requestform, file):
        username = requestform.username.data
        email = requestform.email.data
        last_name = requestform.last_name.data
        first_name = requestform.first_name.data
        password = requestform.password.data
         
        #Guardar la imagen
        if file.filename == '':
            image_name = ''
        else:
            image_name = secure_filename(file.filename)
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image_name)
            file.save(image_path)
        #Verificamos si el nombre de usuario o email ya estan en uso
        user = db.session.query(User).filter(or_(User.username == username, User.email == email)).first()
        if  user:
            return False
        else:
            nuevo = User(
                    email=email, last_name=last_name, first_name=first_name,
                    password=password, username=username,
                    image_name=image_name)
            roles = db.session.query(Rol).filter_by(name="user").first()
            nuevo.roles.append(roles)
            db.session.add(nuevo)
            db.session.commit()
            return True
  


    def getAll():
        return db.session.query(User).filter(User.id!=session["idUserLogged"])

    def getUserByEmailAndPassword(em,pas):
        return  db.session.query(User).filter_by(email=em,password=pas).first() 

    
    #Funcion de busqueda de usuarios
    #inicialmente busco por nombre de usuario que es unico, luego voy a buscar por activo o bloqueado, que trae mas resultados
    #pero esto una vez que este lista la tabla de usuarios con los campos necesarios
    def search(requestform):
         usernam = requestform.get("search")
         actdeact = requestform.get("active")
         #Si no ingresan string a buscar, traigo todos los usuarios, verificando si mandaron activos o bloqueados.
         if not usernam:
             users = db.session.query(User).filter(User.active == actdeact, User.id!=session["idUserLogged"])
         else: 
             users = db.session.query(User).filter(User.username.like('%'+usernam+'%'), User.active == actdeact, User.id!=session["idUserLogged"])
         return users

    def block(requestForm):
        idUser = requestForm['id']
        user = db.session.query(User).filter(User.id == idUser).first()
        #Reviso si el usuario a bloquear es un administrador. Si es, devuelvo false para que no puedan bloquearlo, si no, lo bloqueo.
        for rol in user.roles:
            if (rol.name == "admin"):
                return False
        user.active = 0
        db.session.commit()
        return True

    def activate(requestForm):
        idd = requestForm['id']
        user = db.session.query(User).filter(User.id == idd).first()
        user.active = 1
        db.session.commit()
        return True

    def trash(requestForm):
        idUser = requestForm['id']
        user = db.session.query(User).filter(User.id == idUser).first()
        #Reviso si el usuario a borrar es un administrador. Si es, devuelvo false para que no puedan bloquearlo, si no, lo bloqueo.
        for rol in user.roles:
           if (rol.name == "admin"):
               return False
        user.deleted = 1 
        db.session.commit()
        return True
    
    def getUserById(requestForm):
        idUser = requestForm
        user = db.session.query(User).filter(User.id == idUser).first()
        return  user

    def updateUser(requestform,file):
         form = UserForm()
         form.username = requestform.get("username")
         form.email = requestform.get("email")
         form.last_name = requestform.get("last_name")
         form.first_name = requestform.get("first_name")
         form.password = requestform.get("password")
         form.image_name = requestform.get("image_name")
         idUser = requestform.get("idUser")
         roles = Rol.getRoles()
         if form.validate():
            user = db.session.query(User).filter(User.id  == idUser).first()
            #verifico que el email haya cambiado, si cambio verifico el nombre de usuario, si cambio, hago todo el update
            if ((form.email != user.email)or(form.username != user.username)):
                if (form.email != user.email):
                    #verifico que el email no esta en uso
                    if (db.session.query(User).filter(User.email == form.email).first()):
                        return 0
                    else:
                        user.email = form.email
                if (form.username != user.username):
                    #verifico que el username no esta en uso
                    if (db.session.query(User).filter(User.username == form.username).first()):
                        return 0  
                    else: 
                        user.username = form.username
            for rol in roles:
                if requestform.get(rol.name):
                    user.roles.append(rol)
                else:
                    if rol in user.roles:
                        user.roles.remove(rol)  
                #Guardar la imagen
            if file.filename == '':
                image_name = ''
            else:
                image_name = secure_filename(file.filename)
                image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image_name)
                file.save(image_path)
                user.image_name=image_name                    
            user.first_name = form.first_name
            user.last_name = form.last_name
            user.password = form.password
            db.session.commit()
            return 1
         else:   
            return 2 