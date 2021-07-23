"""
    Nutzung und Konfiguration von dem Python logging Modul:
        Viele Programmierer benutzen zur Fehlersuche die Funktion print.
        Oft werden die Funktionsaufrufe danach auskommentiert oder gelöscht.
        Stattdessen würde ich eher empfehlen, mit dem konfigurierbaren Python logging Modul zu arbeiten.
        Grund dafür ist, dass man dieses auch in produktiven Anwendungen beibehalten kann.

        Um logging zu nutzen, kannst du das Modul einfach importieren. Dieses stellt mehrere Funktionen bereit,
        die du nutzen kannst, um Meldungen auszugeben. Diese unterscheiden sich nach ihrem Level.
        Standardmäßig gibt es die Level debug, info, warning, error und critical.
"""

import logging

#
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

"""
    Anhand des Beispiels siehst du, dass nur die Nachrichten von warning, error und critical ausgegeben wurden. 
    Das liegt daran, dass der Level in logging standardmäßig so konfiguriert ist, 
    dass nur diese ausgegeben werden. Mit der Funktion basicConfig kannst du diesen anders konfigurieren:
"""

# logging.basicConfig(level=logging.DEBUG)
#
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

"""
    Zusätzlich kannst du an basicConfig noch den Parameter filename übergeben, 
    welcher der Name der Datei ist, in der das Log gespeichert werden soll. 
    Standardmäßig werden die Nachrichten nur im terminal ausgegeben.
"""

# logging.basicConfig(filename="logging_1.log", level=logging.DEBUG)
#
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

"""
    Wenn es nicht anders festlegst, wird die Logdatei bei jeder Ausführung des Programms erweitert. 
    Dies wird durch den Dateimodus festgelegt, mit dem die Datei geöffnet wird. 
    Diesen kannst du mit dem Parameter filemode beeinflussen.
"""
#
# logging.basicConfig(filename="logging_1.log", filemode="w", level=logging.DEBUG)
#
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

"""
    Es kann zudem noch ein String angegeben werden, der beeinflusst was im Logfile angezeigt werden soll.
    Dafür können wir den Parameter format verwenden.
"""

# logging.basicConfig(filename="logging_1.log",
#                     filemode="w",
#                     level=logging.DEBUG,
#                     format="%(asctime)s %(levelname)s: %(message)s")
#
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

"""
    Das Format der Uhrzeit kann ebenfalls angepasst werden. Dazu können wir über den Parameter datefmt ein 
    Formatierungscode übergeben. Die Codes sind die selben wie für das Datetime Module
"""

logging.basicConfig(filename="logging_1.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s: %(message)s",
                    datefmt="%d.%m.%Y %H:%M:%S")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
