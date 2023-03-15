import  sqlite3


#kapcsolat letrehozasa
conn = sqlite3.connect("adatbazis.db")

conn.close()