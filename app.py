from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.execute("PRAGMA foreign_keys = ON")
        g.db.row_factory = sqlite3.Row

    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)

    if db is not None:
        db.close()

@app.route("/")
def index():
    return render_template("index.html")