import  sqlite3


#kapcsolat letrehozasa
conn = sqlite3.connect("adatbazis.db")
curs = conn.cursor()#erre van szükségem hogy az sql parancsokat beírni

#letrehoztam a tablat és "oszlopt"
#ez volt az alap de jogosan already exit hibat dob masodik futasra
#curs.execute("CREATE TABLE felhasznalok(nev TEXT, kor INTIGER, nem TEXT, pontszam REAL)")

curs.execute("CREATE TABLE IF NOT EXISTS felhasznalok(nev TEXT, kor INTIGER, nem TEXT, pontszam REAL)")

curs.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, age INTIGER, gender TEXT, score REAL)")

#felhasznalo hozzaadasa
#azért lettek kikommentelve hogy mikor lefuttatom ne adja ujra hozzá
#curs.execute("INSERT INTO felhasznalok VALUES ('Erika', 28, 'Nő', 8.1)")
#curs.execute("INSERT INTO felhasznalok VALUES ('Évi', 34, 'Nő', 8.12)")
#curs.execute("INSERT INTO felhasznalok VALUES ('Zoli', 41, 'Férfi', 7.1)")
#curs.execute("INSERT INTO felhasznalok VALUES ('Pista', 51, 'Férfi', 3.1)")

"""
#azért van kommentelve ne adja újra hozzá köv. futtatáskor 
curs.execute("INSERT INTO users VALUES ('John', 28, 'man', 7.1)")
curs.execute("INSERT INTO users VALUES ('Jack', 48, 'man', 7.7)")
curs.execute("INSERT INTO users VALUES ('ANgelina', 21, 'woman', 7.9)")
curs.execute("INSERT INTO users VALUES ('Hilary', 48, 'woman', 5.2)")
"""

#ez a sor nélkül beleinserteli de nem írja ki
conn.commit()

conn.close()