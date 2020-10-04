from flask import redirect, render_template, request, url_for, session, abort
from app.models.user import User
from app.helpers.auth import authenticated
from sqlalchemy.orm import sessionmaker
from app import db

# Protected resources
def index():
    if not authenticated(session):
        abort(401)
<<<<<<< HEAD

    users = db.session.query(User).all()

=======
    users = session_db.query(User).all()
>>>>>>> 9341b4ab120a386f67c528cf4ed75cae9a530909
    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")


def create():
    if not authenticated(session):
        abort(401)

    User.create(request.form)

    return redirect(url_for("user_index"))
