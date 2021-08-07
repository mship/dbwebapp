import sqlite3
import random
numflights = 500
con = sqlite3.connect("stations.db")
cur = con.cursor()
stations = ['Pegasus', 'Oceanus', 'Epsilon', 'New Las Vegas', 'Persephone', 'Central', 'Wilderness Adventure', 'Enterprise', 'Sandcastle', 'Virgo']
times = []
for i in range(24):
    times.append(i)
for i in stations:
    cur.execute(f"INSERT INTO Stations (name, bays, xloc, yloc) VALUES ('{i}', {random.randint(5, 10)}, {random.randint(0, 5000)}, {random.randint(0, 5000)});")
for i in range(numflights):
    passengermax = random.randint(30, 200)
    cur.execute(f"INSERT INTO Flights (source, dest, departuretime, arrivaltime, passengermax, passengers) VALUES ('{random.choice(stations)}', '{random.choice(stations)}', {random.choice(times)}, {random.choice(times)}, {passengermax}, {random.randint(0, passengermax)});")



con.commit()
con.close()