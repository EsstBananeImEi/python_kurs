1. flask db init
2. flask db migrate -m "users table"
3. flask db upgrade
2. flask db migrate -m "posts table"
3. flask db upgrade

Neue Felder Updaten:
1. flask db migrate -m "new fields in user model"
2. flask db upgrade



PyBabel:
> pybabel extract -F babel.cfg -k _l -o messages.pot .

Extrahiert alle markierten strings in eine .pot

> pybabel init -i messages.pot -d app/translations -l de 
    
Erstellt aus der .pot datei unter app/translations/de eine messages.po datei

> pybabel compile -d app/translations

Kompiliert alle .po Dateien zu .mo

> pybabel update -i messages.pot -d app/translations

Updatet alle .po dateien unter app/translations und fügt neue strings hinzu
damit diese übersetzt werden können.