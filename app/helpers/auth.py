def authenticated(session):
    """Devuelve si el usuario se encuentra en la session"""
    return session.get("user")
