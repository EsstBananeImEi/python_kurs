"""
Typ: Datei Docsting
Inhalt:
    - es gibt 3 arten von Docstrings
        - Der Datei Docstring am anfang einer datei
        - Der Klassen Docstring innerhalb einer Klasse
        - Der Methoden Dockstring innerhalb von Methoden
    - Sie können zu Dokumentations zwecken dienen und sogar ausgegeben werden
"""

class DocstringTest():
    """
    Typ: Klassen Docsting
    Inhalt: zum beispiel informationen über eine Klasse
    """

    def docstring_in_method(self):
        """
        Typ: Methoden Docsting
        Inhalt: zum beispiel informationen über eine methode wie parameter und rückgabe werte
        :return:
        """

print(__doc__)
print(DocstringTest().__doc__)
print(DocstringTest().docstring_in_method.__doc__)