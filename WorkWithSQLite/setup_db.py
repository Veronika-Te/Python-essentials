import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "chinook.db")

def run_query(query, params=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    results=[]
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        if query.strip().upper().startswith("SELECT"):
          results = cursor.fetchall()
        else:
          conn.commit() # Commit changes for CREATE, INSERT, UPDATE, DELETE
    # except sqlite3.OperationalError as e:
    #     print(f"SQLite error: {e}")
    #     results = []
    finally:
        conn.close()

    return results
  
# ------------------------------------------------
# SQL QUERIES 
# ------------------------------------------------

#Artists
create_table_artists = """CREATE TABLE IF NOT EXISTS artists(
  ArtistId INTEGER PRIMARY KEY,
  Name TEXT
);
"""

insert_artists = """INSERT OR IGNORE INTO artists (ArtistId, Name) 
VALUES (1, 'AC/DC'), (2, 'Queen'), (3, 'Metallica'), (4, 'Coldplay');"""

#Albums
create_table_albums="""CREATE TABLE  IF NOT EXISTS albums(
  AlbumId INTEGER PRIMARY KEY,
  Title TEXT,
  ArtistId INTEGER,
  FOREIGN KEY(ArtistId) REFERENCES artists(ArtistId));"""

insert_albums="""INSERT OR IGNORE INTO albums (AlbumId, Title, ArtistId) VALUES 
(1, 'Back in Black' , 1),
(2, 'A Night at the Opera', 2),
(3, 'Black Album', 3),
(4, 'Parachutes', 4);
"""
#Customers
create_table_customers="""CREATE TABLE  IF NOT EXISTS customers(
  CustomerId INTEGER PRIMARY KEY,
  FirstName TEXT,
  LastName TEXT,
  Country TEXT,
  Email TEXT
);
"""
insert_table_customers="""INSERT OR IGNORE INTO customers (CustomerId, FirstName, LastName, Country, Email) VALUES
(1, 'John', 'Smith', 'USA', 'john@example.com'),
(2, 'Anna', 'Schmidt', 'Germany', 'anna@example.com'),
(3, 'Mark', 'Davis', 'USA', 'mark@example.com'),
(4, 'Lena', 'Müller', 'Germany', 'lena@example.com');"""

#Tracks
create_table_tracks="""CREATE TABLE IF NOT EXISTS tracks(
  TrackId INTEGER PRIMARY KEY,
  Name TEXT,
  AlbumId INTEGER,
  UnitPrice REAL,
  FOREIGN KEY (AlbumId) REFERENCES albums(AlbumId)
);
"""

insert_tracks="""INSERT OR IGNORE INTO tracks (TrackId, Name, AlbumId, UnitPrice) VALUES
(1, 'Track A', 1, 0.99),
(2, 'Track B', 2, 1.29),
(3, 'Track C', 3, 1.99),
(4, 'Track D', 4, 0.89),
(5, 'Track E', 3, 1.49);
"""



if __name__ == "__main__":
  # Create tables
  run_query(create_table_artists)
  run_query(create_table_albums)
  run_query(create_table_customers)
  run_query(create_table_tracks)
    
  # Insert data
  run_query(insert_artists)
  run_query(insert_albums)
  run_query(insert_table_customers)
  run_query(insert_tracks) 

  #SELECT
  select_query = "SELECT * FROM albums;"
  results = run_query(select_query)
  for row in results:
    print(row)