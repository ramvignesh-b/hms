from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY']="jhbsdkjhaskdn"

if __name__ == '__main__':
    app.run(debug=True)

#Importing routes.py
from hms import Routes