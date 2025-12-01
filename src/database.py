from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask import Flask
import pyodbc

app = Flask(__name__)

# Inline URI — replace with your actual connection string
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mssql+pyodbc:///?odbc_connect="
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-I8SIAP3;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
)

db = SQLAlchemy(app)

# Example query
with app.app_context():
    result = db.session.execute(text("SELECT * from pkr.hands"))
    print((result.fetchall()))
