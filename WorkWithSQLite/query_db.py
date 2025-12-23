import sqlite3

conn = sqlite3.connect("chinook.db")  
cursor = conn.cursor()
# 1)
# cursor.execute("SELECT * FROM artists")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)
