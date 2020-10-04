import pymysql

from flask import current_app
from flask import g
from flask import cli
from sqlalchemy import create_engine


def connection():
    if "db_conn" not in g:
        config = current_app.config
        g.db_conn = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
    return g.db_conn


def close(e=None):
    conn = g.pop("db_conn", None)

    #if conn is not None:
    #    conn.close()


