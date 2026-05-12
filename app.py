from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# required dummy database for migration setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def home():
    return "SQL Lab Running"


if __name__ == "__main__":
    app.run(debug=True)