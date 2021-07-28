"""
    Aufgabe 1
        1. Erstelle eine Funktion, die einen integer erhält und diesen in einer globalen liste speichern soll.
        2. starte einen neuen Thread mit dieser funktion und übergib eine zahl als parameter
        3. die funktion sollte einen timeout von 1 sekunde haben
        3. gib die liste aus

    Aufgabe 2
        1. modifiziere deinen Code so, das du 10 threads erstellst, die deiner funktion eine nummerierung mitgibt, um
            zu ermitteln welcher thread wann etwas in die liste hinzugefügt hat. lasse die Threads einzeln starten.
            die liste sollte von 0-9 gehen.
        2. nun lasse die Threads parallel laufen, deine liste sollte nun durcheinander sein.

    Aufgabe 3
        1. füge zusätzlich noch einen Thread hinzu der erst nach 5 sekunden die funktion startet (nimm die threading methoden)
            und als zahl die 1337 übergibt
        2. nutze kein join(), sondern warte mit hilfe der is_alive() funktion bis der Thread geschlossen ist bis du die
            liste ausgibst
"""
