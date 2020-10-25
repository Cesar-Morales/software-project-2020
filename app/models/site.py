from app import db


class Site(db.Model):
    
    #El id esta de más si no me equivoco porque va a ser solo uno en todo el sistema
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    pages = db.Column(db.Integer, nullable=False, default=25)
    active = db.Column(db.Boolean, default=True)
    
    def page():
        sitio = db.session.query(Site).first()
        return sitio.pages

    def obtain_site():
        """Metodo que devuelve objeto de configuracion del sitio"""
        return db.session.query(Site).first()
        
    def update_data(title, description, email, pages, active):
        """Funcion que actualiza los datos del sitio, segun parametros."""
        site = db.session.query(Site).first()
        site.title = title
        site.description = description
        site.email = email
        site.pages = pages
        site.active = active
        db.session.commit()
