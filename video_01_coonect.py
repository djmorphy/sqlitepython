import  sqlite3


#kapcsolat letrehozasa
conn = sqlite3.connect("adatbazis.db")
curs = conn.cursor()#erre van szükségem hogy az sql parancsokat beírni

#letrehoztam a tablat és "oszlopt"
#ez volt az alap de jogosan already exit hibat dob masodik futasra
#curs.execute("CREATE TABLE felhasznalok(nev TEXT, kor INTIGER, nem TEXT, pontszam REAL)")

curs.execute("CREATE TABLE IF NOT EXISTS felhasznalok(nev TEXT, kor INTIGER, nem TEXT, pontszam REAL)")


curs.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, age INTIGER, gender TEXT, score REAL)")



conn.close()