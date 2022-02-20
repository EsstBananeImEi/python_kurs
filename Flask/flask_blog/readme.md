1. Virtuelle umgebung installieren
    python -m venv <name der umgebung>
    > python -m venv env
2. erstellen der hello.py mit folgendem inhalt

    from flask import Flask

    app = Flask(__name__)


    @app.route('/')
    def hello():
        return 'Hello, World!'
    
3. Umgebungs variable einstellen.
    - Bash: export FLASK_APP=hello
    - Fish: set -x FLASK_APP hello
    - CMD: set FLASK_APP=hello
    - PS: $env:FLASK_APP = "hello"

4. App Starten:
    > flask run