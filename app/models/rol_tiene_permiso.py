from app import db
"""Archivo para relacionar permisos con roles"""
rol_tiene_permiso = db.Table('rol_tiene_permiso',
db.Column('rol_id', db.ForeignKey('rol.id'), primary_key=True),
db.Column('permiso_id', db.ForeignKey('permiso.id'), primary_key=True),
extend_existing=True)
