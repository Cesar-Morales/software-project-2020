from app import db
from sqlalchemy import or_
from app.models.usuario_tiene_rol import usuario_tiene_rol


class User(db.Model):

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
            db.session.add(nuevo)
            db.session.commit() 
            return True  

    #Funcion de busqueda de usuarios
    #inicialmente busco por nombre de usuario que es unico, luego voy a buscar por activo o bloqueado, que trae mas resultados
    #pero esto una vez que este lista la tabla de usuarios con los campos necesarios
    def search(requestform):
         usernam = requestform.get("search")
         users = db.session.query(User).filter(User.username.like('%'+usernam+'%')).all()
         return users
