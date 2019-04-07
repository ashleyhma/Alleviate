from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)
import os
from flask_sqlalchemy import SQLAlchemy
from model import *
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def homepage():



    return render_template("homepage.html")

@app.route('/register')
def register_form():



    return render_template("register.html")


@app.route('/portal')
def show_portal():



    return render_template("portal.html")




if __name__ == '__main__':

    app.run(port=5000, host='0.0.0.0', debug=True)