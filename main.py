
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3

filepath = os.path.abspath(os.getcwd())+"\stations.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+filepath
db = SQLAlchemy(app)

@app.route('/', methods = ['GET', 'POST'])
def home():

    return render_template('home.html')

@app.route('/flights', methods = ['GET', 'POST'])
def flights():
    # maybe do some filtering on this 
    con = sqlite3.connect("stations.db")
    cur = con.cursor()
    flights = cur.execute("select * from Flights where passengermax > passengers;")
    return render_template('flights.html', flights=flights)

@app.route('/stations', methods = ['GET', 'POST'])
def stations():
    con = sqlite3.connect("stations.db")
    cur = con.cursor()
    if request.method == 'POST':
        form_data = request.form
        cur.execute("PRAGMA foreign_keys=ON;")
        cur.execute("delete from Stations where name = ?;", (form_data['Close'], ))
        
        stations = cur.execute("select * from Stations;")
        con.commit()
        return render_template('stations.html', stations=stations, form_data = form_data)
    stations = con.execute("select * from Stations;")
    return render_template('stations.html', stations=stations)

@app.route('/cancel', methods = ['GET', 'POST'])
def cancel():
    # need to put passengers on next flight if one is canceled
    con = sqlite3.connect("stations.db")
    cur = con.cursor()
    cur.execute("select source, dest from Flights where id = 0")
    cur.execute("delete from Flights where id = 0")

    return render_template('flights.html')

@app.route('/stationadmin')
def stationadmin():
    # deleting items that are foreign keys in other tables
    # if a station is closed, all flights will be canceled
  
    return render_template('stationadmin.html')

@app.route('/newflights', methods = ['GET', 'POST'])
def newflights():
    return render_template('flights.html')