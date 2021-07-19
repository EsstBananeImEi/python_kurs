"""
    Die Kommandozeile auch als CLI (Command Line Interface) bezeichnet, wird verwendet um Kommandos in Textform
    an ein Programm zu übergeben zu können. Mit hoher warscheinlichkeit hast du dies auch schon einmal getan. Denn
    Grundsätzlich ist dies keine große Sache, da sich die Anwendung wirklich einfach gestaltet.

    In Python existieren zahlreiche Bibliotheken mit denen wir CLI Anwendungen erzeugen können. In den meistenfällen
    wird jedoch die argparse Bibliothek verwendet, um Kommandos an das Programm zu übergeben

    In dieser Lektion werden wir uns damit beschäftigen wie wir eine Solche kleine CLI erstellen und parameter übergeben können.
"""

# def display_message(message):
#     print(f"Message: {message}")
#
# display_message("Hallo Welt")

"""
    Um die display_message()-Methode nun so nutzen zu können, das ein User eine nachricht vorgibt die wir mittels
    print()-Methode ausgeben müssen wir einen input erstellen und die nachricht an die methode übergeben.
"""
#
# message = input("Bitte eine nachricht eingeben\n")
# display_message(message)

"""
    Dies stellt bis dahin kein Problem dar, aber was ist wenn wir nun das ganze über das Terminal starten 
    und ein argument übergeben wollen.
    
    Natürlich funktioniert das ausführen des Programms wie erwartet, nun wollen wir aber die eingabe nicht per
    input tätigen, sondern wir möchten es als parameter übergeben. Dies können wir mithilfe von argparse implementieren
"""

import argparse
import sys


def demo():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "-n",
            "--nachricht",
            type=str,
            default="Keine nachricht vorhanden",
            help="Schreib eine Nachricht...",
    )
    arguments = parser.parse_args()
    display(arguments)


def display(arguments):
    sys.stdout.write(str(arguments.nachricht))


if __name__ == "__main__":
    demo()

"""
    Jetzt haben wir unseren finalen Code. Bevor wir diesen allerdings ausführen, 
    besprechen wir doch kurz die wichtigsten Schritte:

    1. Um die argparse-Bibliothek zu nutzen, haben wir diese zunächst importiert.
    
    2. In der demo()-Funktion haben wir mittels der ArgumentParser()-Funktion aus dem argparse-Modul einen Parser erstellt.
    
    3. Den Parser haben wir anschließend genutzt, um Argumente mittels der add_argument()-Funktion hinzuzufügen.
    
    4. Die add_argument()-Funktion erfordert vier Argumente:
        Name des Arguments, Datentyp des Arguments, Standardwert, Hilfsnachricht.
        
        Wir haben zwei Namen für das Argument festgelegt
    
    5. Nach dem Erstellen des Arguments haben wir die parse_args()-Funktion benutzt, 
        um die Argumente aus der Kommandozeile zu extrahieren. 
        Diese haben wir dann in der Variable „arguments“ gespeichert und schließlich als Argument an die display()-Funktion übergeben.
        
    Führen wir den Code nun über das Terminal aus.
    
    
    Wie wir sehen funktioniert unser Code.

    Das Kommando, das wir eigegeben haben, lautet wie folgt: python _argparse.py –n=“Hallo Welt!“
    
        _argparse.py ist der name der Datei die wir ausführen wollen
        -n ist das Argument das wir mithilfe der add_argument()-Methode hinzugefügt haben.
        “Hallo Welt!“ ist die Nachricht die wir übergeben
    
    Wir haben auch eine Hilfenachricht festgelegt, schauen wir uns nun an wie wir diese sehen.
    
    Durch das Kommando python _argparse.py –h sagen wir dem Programm das wir die Hilfe angezeigt haben möchten.
    Dort finden wir alle Argumente und deren Hilfenachricht die wir definiert haben wieder.
"""
