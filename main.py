from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mssql+pyodbc:///?odbc_connect="
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-I8SIAP3;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
)
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

# Demo state endpoint; swap with real game state
@app.route("/api/state")
def state():
    sample = {
        "pot": 320,
        "community": ["Q♥", "7♣", "7♦", "—", "—"],
        "players": [
            {"name": "You", "stack": 950, "bet": 50, "status": "To act", "is_self": True},
            {"name": "Ava", "stack": 1200, "bet": 80, "status": "Thinking"},
            {"name": "Ben", "stack": 610, "bet": 40, "status": "Folded"},
        ],
        "hand": ["A♠", "K♠"]
    }
    return jsonify(sample)
