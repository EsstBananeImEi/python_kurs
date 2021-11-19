"""
    #### Aufgabe 1 ####
    Es wird eine Klasse benötigt, mit der man Personen mit folgenden eigenschaften 
    erstellen kann, die eigenschaften sollen nicht über den Konstruktor gesetzt werden:

    - Name
    - Alter
    - Geschlecht

    Es wird für jede Eigenschaft eine Funktion benötigt um den wert zu setzen (Setter),
    zudem soll es eine Funktion "birthday" geben, 
    die das alter um 1 erhöht wenn sie aufgerufen wird und eine Funktion talk mit
    der sich die person vorstellen kann (Mein name ist ... ich bin ... jahre alt).

    Nach der Implementierung teste deine Klasse:
        1. Erzeuge ein Objekt der Klasse Person. Speichere dabei das Objekt in einer Variablen person.
        2. Setze den Namen des Objekts auf Alice.
        3. Setze das Alter des Objekts auf 22.
        4. Lasse die Person sprechen.
        5. Lasse die Person ihren Geburtstag feiern. 
        6. Überprüfe mit der Methode talk(), ob das Alter
            um eins erhöht wurde



    #### Aufgabe 2 ####
    Es wird eine Neue Klasse namens Mensch gewünscht die ihre eigenschaften und methoden
    an eine Person vererbt. Zudem wird eine Neue Eigenschaft "augenfarbe" gewünscht, 
    sowie eine methode um die Augenfarbe zu setzen. Wenn die Person sich vorstellt,
    soll die Augenfarbe ebenfalls vorkommen wenn sie gesetzt ist.
    

    Teste wieder deine Implementierung:
        1. Erzeige ein Objekt der Klasse Person. Speichere das Objekt in der Variable "Petra"
        2. Setze den Namen des Objekts auf Petra.
        3. Setze das Alter des Objekts auf 44.
        5. Lasse die Person sprechen.
        7. Überprüfe mit der Methode talk(), ob das Alter
            um eins erhöht wurde (ohne Augenfarbe)
        7. Setze die Augenfarbe auf "Blau"
        8. Überprüfe wieder über die Methode talk(), 
            ob nun auch die Augenfarbe ausgegeben wird. 



    #### Aufgabe 3 ####
    Es wird ein Programm benötigt in dem wir einer Person 
    (nennen wir die Person mal "Programmierer") ein Arbeitsgerät Laptop oder DesktopPc 
    zugewiesen werden kann.
    
    Die Arbeitsgeräte benötigen die Eigenschaften und Methoden für:

    - Eigenschaften:
        - die Architekture (64 oder 32 bit)
        - das Betriebssystem (Windows / Linx...)
    - Methoden:
        - das Starten eines Prozesses, dieser Prozess soll z.b folgendes ausgeben:
            - Starte Laptop Prozess für \<Windows> <64 bit>

    Für den Programmierer werden die Eigenschaften und Methoden:

    - Eigenschaften:
        - für den Name
        - für das Team in dem er eingesetzt ist
    - Methoden:
        - für das aufnehmen seiner Arbeit, diese Funktion soll folgende aufgaben haben:
            - Das ausgeben einer Nachricht, das er seine Arbeit beginnt
            - Das ausführen der Funktion um den Prozess von Laptop oder DesktopPc zu starten
        - um die Aktiven Programmierer anzuzeigen

    Wenn er Programmierer seine Arbeit aufnimmt soll er einer Liste hinzugefügt 
    werden um diese über eine Seperate Funktion abzufragen, 
    die Funktion soll auch über die Klasse aufrufbar sein (Programmierer.deine_methode()).
    Wenn ein Programmierer "Zerstört" wird, soll er aus der Liste entfernt werden.

    - Tips:
        1. Lasse Laptop und DesktopPc von einer Mutterklasse Erben, 
            falls du nicht weißt was gemeint ist, 
            überlege dir "Was ist ein Laptop und was ist ein DesktopPc im Allgemeinen"
        2. Aktive Programmierer Anzeigen, denke daran das es verschiedene 
            Arten von Methoden gibt staticmethod... 
            mit einer dieser methoden kannst du dies umsetzen.
        3. Zum Entfernen des Programmierers aus der liste, 
            brauchst du den gegenpart zum Konstruktor.
        
"""
