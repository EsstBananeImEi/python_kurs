"""
Frage 1: Mit Welchem Befehl werden die Threads erstellt ?

    A.) acquire()
    B.) run()
    C.) start()
    D.) lock()

    Richtige Lösung: C
"""

"""
Frage 2: wie sagen wir dem MainThread, das auf andere Threads gewartet werden soll ?

    A.) stop()
    B.) wait()
    C.) acquire()
    D.) join() 

    Richtige Lösung: D
"""

"""
Frage 3: was macht das acquire() ?

    A.) es hält einen Thread an.
    B.) es entsperrt einen Thread
    C.) es aktiviert die Sperre.

    Richtige Lösung: C
"""

"""
Frage 4: Was welches der folgenden Probleme können beim Sperren von Threads auftreten ?

    A.) ein Thread wird mehrfach ausgeführt.
    B.) alle Threads werden mehrfach ausgeführt.
    C.) es können keine Probleme auftreten.
    D.) es könnte durch das Aktivieren einer Sperre und dem erneuten aufrufen von acquiere in z.b der selben funktion, 
        eine Deadlock auftreten, wodurch der MainThread nicht mehr weiter läuft.

    Richtige Lösung: D
"""
