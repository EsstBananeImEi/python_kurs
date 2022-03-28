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


Raspberry Pie 

Root User sonst sudo

apt update
apt upgrade

wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0
tar -zxvf Python-3.10.0.tgz

cd Python-3.10.0
./configure --enable-optimizations
make altinstall

python3.10 als python

cd /usr/bin
sudo rm python
sudo ln -s /usr/local/bin/python3.9 python
python --version


1. copy projekt
2. change flask_blog.py 
    if __name__=='__main__':
        app.init_app()
        app.run(host='<raspi ip>')

        ....
3. create systemd <service name>.service
    [Unit]
    Description=Flask Blog service

    [Install]
    WantedBy=multi-user.target

    [Service]
    Type=simple
    User=root

    WorkingDirectory=<path to Blog>
    Environment="PATH=$VIRTUAL_ENV/bin:$PATH"
    ExecStart=<path to flask_blog.py> --host=192.168.2.108

4. systemctl daemon-reload
5. systemctl start <service name>.service
6. systemctl status <service name>.service
7. http://<raspi ip>:5000
