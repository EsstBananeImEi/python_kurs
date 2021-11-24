"""
    # Aufgabe Exceptions

    In diesem Abschnitt, hat jede aufgabe ihren Eigenen Codeblock, kopiere dir den jeweiligen abschnitt in deine Python umgebung und löse die Aufgabe.

    ### Aufgabe 1

    Der folgende Code bricht mit einer Exception ab. Kümmere dich um das Exception Handling und gib eine entsprechende Nachricht aus, wenn die Exception auftritt.

    ```python
        import helper

        def read_file():
            with open("throw.txt", "r") as file:
                file.read()

        read_file()
        helper.im_running()
    ```

    ### Aufgabe 2

    Folgender Code soll sich Daten aus einer SQL Connection holen. 

    ```python
        import helper
        def get_sql_data():
            connection = helper.SqlConnection()
            connection.connect()
            return connection.get_data()
            
        data = get_sql_data()

        if data is not None:
            data = helper.transform_data(data)
        helper.im_running()
    ```

    Ändere den Code so ab, das bei einer Exception ein None zurückgegeben wird und die Exception geloggt wird. Da wir das Thema logging noch nicht behandelt haben nehmen wird stellvertretend für das logging ein print mit "logge Fehler" oder nutze die Exception um eine Ausgabe zu erstellen

    - Tip:
        - Try, Except, Finally wird dir dabei helfen ein None zurück zu geben.

    ### Aufgabe 3

    Es wird die Methode number_check die ein Parameter erhält und einen Integer (Zahl) zurückgibt. Sollte der Parameter kein Integer (Zahl) sein oder sollte der Integer (Zahl) eine 0 sein, dann wird jeweils eine Eigene Exception Klasse benötigt. Die Namen der Exception Klassen sind frei wählbar.
    
    - Die Exception Klasse falls es sich nicht um einen Integer handelt, soll bei der Initialisierung den Integer übergeben gekommen um daraus die Exception "... is not a number" zu generieren.

    - Die andere Exception Klasse benötigt keinen Parameter und soll nur die Exception "number cant be zero" ausgeben.

    Falls die Aufgabe noch zu schwierig ist, nutze gerne die Tips.  

    - Tips:
        1. Erstelle die erste Exception Klasse
            - Namensvorschlag: NumberFormatException
            - füge dem Konstruktor den Parameter value hinzu.
            - erstelle aus dem Parameter die Nachricht "... is not a number"
            - gibt die Nachricht an den Konstruktor der Mutterklasse weiter
        2. Erstelle die zweite Exception Klasse
            - Namensvorschlag: NumberNotZeroException
            - erstelle die Nachricht "number cant be zero" und gib diese an die Mutterklasse weiter.
        3. Erstelle die Methode number_check die den Parameter number entgegen nimmt.
            - Prüfe nun ob number eine Zahl ist (google ist dein Freund)
                - Wenn Ja dann wirf die NumberFormatException(number)
            - Nun Prüfe nochmals ob number gleich 0 ist
                - Wenn Ja dann wirf die NumberNotZeroException()
            - Wenn nichts zutrifft lasse den wert number über einen print ausgeben.
        
"""
