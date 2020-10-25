"""
Turnos creados por operator para que luego en la app publica seleccionen
"""
from app import db

class Centro(db.Model):

    id = db.Column(db.Integer, primary_key=True, 
                   nullable=False, 
                   autoincrement=True)
    start_time = db.Column(db.String(80), nullable=False)
    final_time = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    selected = db.Column(db.Boolean, default=False)

    centro_id = db.Column(db.Integer, 
                          db.ForeignKey('centro.id'),
                          nullable=False)
