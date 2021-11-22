"""
    Mit dem Finally block können wir selbst nach einer Exception das Programm weiterlaufen lassen
    Dies ist zum beispiel wichtig wenn wir eine API bereitstellen und jemand daten Anfragt, bei denen wir während
    der bereitstellung eine Exception erhalten, wollten wir trozdem etwas zurückgeben z.b ein None, einen Fehlercode 500
    oder irgend etwas anderes.

    Dann benötigen wir das Finally
"""


def backend_answer():
    return_value = 500
    try:
        print(5 / 0)
        return_value = {"display_name": "App",
                        "subtitle": "Subtitle Text",
                        "values": []}
    except Exception:
        print("Logge Fehler in Datei")
    finally:
        return return_value


# Aus sicht des frontends
# anfrage senden:
answer = backend_answer()
# antwort verarbeiten
if answer is not None \
        and not answer == 500 \
        and not answer == 505 \
        and not answer == 404:
    print("tue etwas logisches")
    print("zeige Frontend an")
else:
    print(f"zeige nutzer fehler eine meldung für error {answer}")
