import  sqlite3
from pprint import pprint

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
curs.execute("INSERT INTO felhasznalok VALUES ('Dani', 20, 'Férfi', 5.2)")

"""
#azért van kommentelve ne adja újra hozzá köv. futtatáskor 
curs.execute("INSERT INTO users VALUES ('John', 28, 'man', 7.1)")
curs.execute("INSERT INTO users VALUES ('Jack', 48, 'man', 7.7)")
curs.execute("INSERT INTO users VALUES ('ANgelina', 21, 'woman', 7.9)")
curs.execute("INSERT INTO users VALUES ('Hilary', 48, 'woman', 5.2)")
"""
curs.execute("UPDATE felhasznalok SET nem=? WHERE nem=?",("nő","Nő"))#a ? az placeholder. mire a mit a sorrend
conn.commit()

curs.execute("UPDATE felhasznalok SET nem=? WHERE nem=?",("férfi","Férfi"))#a ? az placeholder. mire a mit a sorrend
conn.commit()


curs.execute("UPDATE users SET gender=? WHERE gender=?",("female","woman"))#a ? az placeholder. mire a mit a sorrend
conn.commit()

curs.execute("UPDATE users SET gender=? WHERE gender=?",("male","man"))#a ? az placeholder. mire a mit a sorrend
conn.commit()

#elirást javítok gyakorlás képpen
curs.execute("UPDATE users SET name=? WHERE name=?",("Angelina","ANgelina"))#a ? az placeholder. mire a mit a sorrend
conn.commit()

#felhasznalok kilistázása
curs.execute("SELECT * FROM felhasznalok")
# fetchall vissza adja az adatokat a táblából
adatok = curs.fetchall()
print(adatok)
pprint(adatok)  #prityprint szebben tördeli

curs.execute("SELECT * FROM users")

adatok2 = curs.fetchall()
print(adatok2)

#csak ha a neveket akarom

curs.execute("SELECT name FROM users")
adatok3 = curs.fetchall()
print(adatok3)


curs.execute("SELECT name, score FROM users")
adatok4 = curs.fetchall()
print(adatok4)


#az adatok tuple-ként jelennek meg, nézd h sima zárójel!!!!!!!
curs.execute("SELECT nev, pontszam FROM felhasznalok")
adatok5 = curs.fetchall()
print(adatok5)

#"primary key"-féle megoldás. SQLite kicsit másképp kezeli a pkey-t
curs.execute("SELECT nev, pontszam FROM felhasznalok WHERE ROWID=1")
adatok6 = curs.fetchall()
print(adatok6)








#ez a sor nélkül beleinserteli de nem írja ki
conn.commit()
conn.close()