import sqlite3

connection = sqlite3.connect("database.db")


with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
    f"INSERT INTO posts (title, content) VALUES ('Python Database Tutorial', 'Du hast erfolgreich die Datenbank eingerichtet.')"
)

cur.execute(
    f"INSERT INTO posts (title, content) VALUES ('Abfragen eines Blog eintrags', 'Schaue dir nun die lektion \"Anzeigen eines Blog eintrags\" an um einzelne einträge anzuzeigen ')"
)

connection.commit()
connection.close()
