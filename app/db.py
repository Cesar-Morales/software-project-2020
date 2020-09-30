import pymysql

from flask import current_app
from flask import g
from flask import cli
from flask_sqlalchemy import SQLAlchemy

def connection():
    if "db_conn" not in g:
        g.db_conn = SQLAlchemy(current_app)
    return g.db_conn


def close(e=None):
    conn = g.pop("db_conn", None)

    if conn is not None:
        conn.close()


def init_app(app):
    app.teardown_appcontext(close)
