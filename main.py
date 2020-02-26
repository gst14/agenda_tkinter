from contacto import Contacto
import sqlite3

con = sqlite3.connect('agenda.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS contactos(id integer PRIMARY KEY, nombre varchar(50) NOT NULL, nrotelefono varchar(50) NOT NULL)")
con.commit()

p = Contacto("Gaston Avila",3816020051)

print(p)