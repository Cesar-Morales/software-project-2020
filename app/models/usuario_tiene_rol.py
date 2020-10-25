from app import db
"""Archivo para relacionar usuarios con roles"""
usuario_tiene_rol = db.Table('usuario_tiene_rol', 
db.Column('rol_id', db.ForeignKey('rol.id'), primary_key=True), 
db.Column('user_id', db.ForeignKey('user.id'), primary_key=True), 
extend_existing=True)