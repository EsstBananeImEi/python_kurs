"""
    Vergleichsoperatoren:
    Operator | Name                     | Example
        ==   | Equal	                | x == y
        !=	 | Not equal	            | x != y
        >	 | Greater than	            | x > y
        <	 | Less than	            | x < y
        >=	 | Greater than or equal to	| x >= y
        <=	 | Less than or equal to	| x <= y

"""
print("#### if 1 ####")
n = 32
x = 40
if n < x:
    print("%s ist kleiner als %s" % (n, x))
print("ich werde auch ausgeführt!")


print("\n#### if 2 ####")
if n < 5:
    print("%s ist kleiner als %s" % (n, 5))
else:
    print("%s ist größer als %s" % (n, 5))


print("\n#### if 3 ####")
is_true = 5 < 10
if is_true:
    print("5 ist kleiner als 10")
