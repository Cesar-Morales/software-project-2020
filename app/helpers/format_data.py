"""
Modulo para definir filtros de jinja para formatear data
"""

from datetime import date

#Filtro para formatear la fecha. HAY QUE CAMBIAR ESTO DE LUGAR CREO
def datetimeformat(value, format='%d-%m-%Y'):
    return date.fromisoformat(value).strftime(format)