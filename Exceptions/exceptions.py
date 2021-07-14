"""
    Beim Schreiben von Code können wir immer wieder einmal fehler machen und es könnte ein verhalten auftreten das
    wir nicht erwartet haben.

    Wo könnten dinge passieren die wir nicht bedacht haben.
    - der versuchen eine ressource zu öffnen die nicht existiert.
    - bei einer division gibt der nutzer 4 / 0 ein, dies wird in einer exception enden.
    ....

"""

"""
    Python Syntax Errors:
    Sind im Allgemeinen fehler die entstehen wenn gegen sogennate syntaktische Regeln verstoßen wird.
    Programme mit Syntaxfehlern werden von einem Compiler oder Interpreter zurückgewiesen
"""
# if a < 3


"""
    Python Logical Errors (Exceptions):
    Sind Fehler die zur laufzeit des Progammes entstehen, sie werden auch Exceptions oder logische fehler gennant
    diese treten z.b beim öffnen einer Datei auf die nicht existiert, beim dividieren durch 0, oder wenn versucht
    wird ein Module zu importieren das nicht existiert. 
"""
# with open("text", "r"):
#     pass


"""
    Python Built-in Exceptions:
    Illegale Operationen können Exceptions auslösen. Es gibt in Python integriert einige Exceptions die ausgelöst
    werden können. 
    Wir können all diese "built-in" Exceptions ausgeben, wenn wir die built-in funktion locals() nutzen
"""
# [print(e) for e in dir(locals()['__builtins__'])]


#
# while True:
#     zahl1 = input("Eingabe zahl 1\n")
#     zahl2 = input("Eingabe zahl 2\n")
#     print(int(zahl1) / int(zahl2))

# with open("test.txt", "r") as file:
#     print(file.read())
#
# print("hier komme ich nicht hin")


#
# try:
#     print(5 / 2)
#     with open("test.txt", "r") as file:
#         print(file.read())
# except ZeroDivisionError:
#     print("Teilen durch 0 ist nicht erlaubt")
# except FileNotFoundError:
#     print("Die Datei existiert nicht")
# print("Ich werde noch ausgeführt")


#
# try:
#     print(5 / 0)
#     with open("test.txt", "r") as file:
#         print(file.read())
# except Exception:
#     print("ein fehler ist aufgetreten")


# def do_something():
#     print(5/0)
#
#
# try:
#     do_something()
# except Exception:
#     raise


d = {"demo": 1,
     "demo2": 2}
try:
    print(d["demo"])
    print(d["demo2"])
    print(d["demo3"])
except KeyError:
    print("Der Schlüssel ist nicht enthalten")

print(d.get("demo3"))
