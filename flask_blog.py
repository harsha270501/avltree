
from flask import Flask,render_template, redirect, url_for,request, flash
from forms import enterDetailsForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ANKILOVESCHOCOLATE07'

formpref=''


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
