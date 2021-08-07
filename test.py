import sqlite3

con = sqlite3.connect("stations.db")
cur = con.cursor()

select = con.execute("select * from Stations;")
con.execute("update Stations set name = 'Pegasus' where name = 'Megan';")
con.commit()
for i in select:
    print(i)