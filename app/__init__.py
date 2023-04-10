"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr115269v5rj89hd80-a",
        database="todo_demo_bjlc        ",
        user="todo_demo_bjlc_user",
        password="hthsVEXQpOrYDwzcMFUT0Q1pNJClh44K")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
