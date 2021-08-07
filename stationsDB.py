import sqlite3

con = sqlite3.connect("stations.db")
con.execute("drop table if exists Flights;")
con.execute("drop table if exists Stations;")
con.execute("drop trigger if exists source_dest_conflict;")
con.execute("create table Stations(name VARCHAR(30) UNIQUE, bays INT, xloc INT, yloc INT);")
con.execute("create table Flights(id INTEGER PRIMARY KEY AUTOINCREMENT, source TEXT NOT NULL, dest TEXT NOT NULL, departuretime TIME, arrivaltime TIME, passengermax INT, \
            passengers INT, FOREIGN KEY(source) REFERENCES Stations(name) on delete cascade, FOREIGN KEY(dest) REFERENCES Stations(name) on delete cascade);")

con.execute("create trigger source_dest_conflict \
            before insert on Flights \
            begin \
                select \
                    case \
                        when NEW.source = NEW.dest  then \
                            raise (IGNORE) \
            end; \
        end;")
con.close()

