"""
  # Regular Expression

    Eine Sequenz aus Zeichen, die ein Suchmuster darstellen, werden in Python „regular expression“, oder auch Python RegEx genannt. Diese Muster werden verwendet, um Strings oder Substrings zu finden. Die „regular expression“ wird für String-Operationen wie find() und replace() verwendet.

    Anders als in anderen Programmiersprachen, besitzt Python für Regular Expression das <code>re</code> modul.
    Regular Expression werden in der regel mit sogenannten Metazeichen geschrieben, hier einige der am meisten genutzen mit ihrer verwendung:
    
    | Meta-Charakter        | Beschreibung                                                                          |
    | \d	                | Eine Ziffer von 0 bis 9                                                               |
    | [a-z] oder [A-Z0-0]   |	Eckige Klammern geben immer ein Set an Ziffern an                                   |
    | \	                    | Backslash escaped Zeichen, die selbst ein regulärer Ausdruck sind                     |
    | a+	                | Links vom + kann a ein oder mehrfach vorkommen                                        |
    | Hallo*	            | Links vom * kann o nicht oder mehrfach vorkommen                                      |
    | k{2,5}                | 	Zwei bis fünf k´s hintereinander                                                    |
    | [^1-3]                | 	Keine 1 bis 3                                                                       |
    | \w	                | Leerzeichen oder Absatz                                                               |
    | aaa?	                | Das letzte a ist optional                                                             |
    | (Sahne\|Obers)        |	oder                                                                                |
    | ^a                    | Prüft ob der String mit a beginnt                                                     |
    | $a                    | Prüft ob der String mit a endet                                                       |
    | a.c                   | Prüft zwischen den Zeichen „a“ und „c“ ob genau ein weiteres Zeichen befindet         |
    | a..c                  | Prüft zwischen den Zeichen „a“ und „c“ ob genau zwei weitere Zeichen befinden usw.    |
    | (a\|b\|)cd            | vor cd kann ein a oder b vorkommen                                                    |
    | b{n,m}                | b muss mindestens n mal vorkommen und maximal m mal vorkommen                         |

    
    Du kannst die folgenden Online-Tools als Sandkasten für Deine Regex-Code verwenden.
    

    - https://regexr.com/
    - https://regex101.com/
    - https://www.regextester.com/
"""

import re

such_muster = "abc"
text = "abc"

""" Das erste Argument der Funktion ist das Muster. Das Zweite ist der entsprechende String. """
print(re.match(such_muster, text))

"""
    Solange das muster und der String genau gleich sind, wird die match()-Methode ein Objekt zurückliefern.
"""
text = "xyz"
print(re.match(such_muster, text))

""" Die match()-Funktion gibt nichts zurück, da das Muster nicht genau dem Text entspricht. """

"""
    Unsere beispiele von eben sind sehr einfach gehalten, und würden in Produktivem Code wohl eher nicht vorkommen. 
    Wir würden sogennante Metazeichen nutzen, um eine Regular Expression zu erzeugen.
    
    In Python gibt es viele dieser Metazeichen. 
    Anhand eines Beispiels werden wir diese besprechen und dabei noch einige Methoden des re-Modules kennenlernen.
    
    Um zu Prüfen ob ein String mit einem bestimmten Zeichen startet, 
    verwenden wir das Einschaltungszeichen "^".
"""

muster = "^h"
text_1 = "hallo"
text_2 = "hi"
text_3 = "tschau"

ergebnis_1 = re.match(muster, text_1)
ergebnis_2 = re.match(muster, text_2)
ergebnis_3 = re.match(muster, text_3)

print(ergebnis_1)
print(ergebnis_2)
print(ergebnis_3)

""" Der erste und zweite String starten jeweils mit einem „h“. Der dritte String wiederum nicht. """

""" 
    Das Dollarzeichen $:
    Wenn wir wiederum nachvollziehen wollen, ob ein String mit einem bestimmten Zeichen endet, 
    verwenden wir das Dollarzeichen "$".
"""

muster = "o$"
text_1 = "hallo"
text_2 = "hi"
ergebnis_1 = re.search(muster, text_1)
ergebnis_2 = re.search(muster, text_2)

print(ergebnis_1)
print(ergebnis_2)

""" 
    Das Eckige Klammern "[]":
    Mit hilfe der eckigen Klammern, können wir Zeichen die in einem String gesucht werden definieren.
"""
muster = "[a-i]"
""" [a-i] beschreibt alle kleinbuchstaben die im Alphabet zwischen a und h stehen"""
text_1 = "Das ist mein kleiner test Text"
""" Diesmal nutzen wir die findall()-Methode, um eine liste der gefunden buchstaben zu erhalten """
ergebnis_1 = re.findall(muster, text_1)
print(ergebnis_1)

"""
    Die Periode ".":
    Wird verwendet um den Sting an einer spezifischen Position auf ein bestimmtes zeichen zu untersuchen.
"""
muster = "l.o"
""" Das Muster erfüllt nur die Prüfung, wenn sich zwischen dem l und dem o nur ein weiteres Zeichen befindet """
text_1 = "hallo"
text_2 = "hi"
text_3 = "Abfallstoff"
ergebnis_1 = re.match(muster, text_1)
ergebnis_2 = re.match(muster, text_2)
ergebnis_3 = re.match(muster, text_3)

print(ergebnis_1)
print(ergebnis_2)
print(ergebnis_3)

"""
    Das Sternsymbol "*":
    Das Sternsymbol erweitert die Funktion des vorherigen Zeichens. 
    Es wird betrachtet, ob das entsprechende Zeichen kein- oder mehrfach zwischen den Buchstaben befindlich ist.
"""

muster = "ab*c"
"""  Das Muster erfüllt nur die Prüfung, wenn sich zwischen dem a und dem c nur null bis mehrere weitere b's befindet  """
text_1 = "abbc"
text_2 = "ac"
text_3 = "abbdbc"
ergebnis_1 = re.match(muster, text_1)
ergebnis_2 = re.match(muster, text_2)
ergebnis_3 = re.match(muster, text_3)

print(ergebnis_1)
print(ergebnis_2)
print(ergebnis_3)

"""
    Das Pluszeichen "+":
    Das Pluszeichen ist da, um zu prüfen, ob das entsprechende Zeichen ein- oder mehrfach an der Stelle vorkommt.
"""

muster = "ab+c"
text_1 = "abbc"
text_2 = "ac"
text_3 = "abbdbc"
ergebnis_1 = re.match(muster, text_1)
ergebnis_2 = re.match(muster, text_2)
ergebnis_3 = re.match(muster, text_3)

print(ergebnis_1)
print(ergebnis_2)
print(ergebnis_3)

""" 
    Der erste und dritte String verhält sich gleich zur Verwendung des Sternsymbols. 
    Der zweite String hingegen wird nicht in das Muster passen, 
    da das Pluszeichen kein Nullvorkommen als gültig erachtet. 
"""

"""
    Die Gruppierung "()":
    Die runden Klammern können zur Gruppierung von Submustern verwendet werden.
"""

muster = "(Hallo|Hi) Welt"
""" Das Muster erfüllt nur die Prüfung, wenn sich vor Welt ein Hallo oder ein Hi befindet  """
text_1 = "Hallo Welt"
text_2 = "Gute Nacht Welt"
text_3 = "Hi Welt"
ergebnis_1 = re.match(muster, text_1)
ergebnis_2 = re.match(muster, text_2)
ergebnis_3 = re.match(muster, text_3)

print(ergebnis_1)
print(ergebnis_2)
print(ergebnis_3)

"""
    Die Geschwungene Klammern "{}":
    Die Klammern geben an, wie oft ein Zeichen mindestens auftreten muss und wie oft ein Zeichen Maximal aufgeführt
    sein darf. 
    
    Die Schreibweise sieht wie folgt aus: 
        "zeichen{minimalwert,maximalwert}"
        "b{2,5}"
"""
muster = "ist{1,3}"
""" Das Muster erfüllt nur die Prüfung, wenn sich mindestens ein - drei "ist" im Satz befinden """
text_1 = "Mein Kopf ist schwer, der ist voll"
text_2 = "ist der gockel platt wie'n teller, war der Tracktor wieder schneller"
text_3 = "Hi Welt"
ergebnis_1 = re.search(muster, text_1)
ergebnis_2 = re.search(muster, text_2)
ergebnis_3 = re.search(muster, text_3)

print(ergebnis_1)
print(ergebnis_2)
print(ergebnis_3)

"""
    Python RegEx mit Sets:
    Oben haben wir bereits die eckigen Klammern verwendet, um Zeichen zu finden. 
    Genauso können wir diese nutzen, um mehrere spezifische Zeichen zu finden.
"""

muster = "[abc]"
""" Der String wird nur in das Muster passen, wenn mindestens ein Zeichen im String auftaucht. """
text_1 = "abcbcbc"
text_2 = "xxxxx"
ergebnis_1 = re.search(muster, text_1)
ergebnis_2 = re.search(muster, text_2)

print(ergebnis_1)
print(ergebnis_2)

"""  
    Das Einschaltungszeichen "^":
    Das Einschaltungszeichen bedeutet, dass der String nicht in das Muster passt, 
    wenn einer der entsprechenden Buchstaben im String zu finden ist.
"""

muster = "[^abc]"
""" Der String wird nur in das Muster passen, wenn mindestens ein Zeichen im String auftaucht. """
text_1 = "abcbcbc"
text_2 = "xxxxx"
ergebnis_1 = re.search(muster, text_1)
ergebnis_2 = re.search(muster, text_2)

print(ergebnis_1)
print(ergebnis_2)

""" 
    Grundsätzlich können wir also jedes gewünschte Muster in unsere eckigen Klammern einfügen. 
    Zum Beispiel wird „[a-z]“ alle Kleinbuchstaben des Alphabets vergleichen. 
    „[A-Z]“ wird alle Großbuchstaben abgleichen. Um gleichzeitig alle Klein- und Großbuchstaben zu untersuchen, 
    könne wir „[a-zA-Z]“ verwenden. Gleichermaßen können wir für die Zahlen „[0-9]“ verwenden
"""
