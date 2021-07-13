"""
    In Python haben wir 3 zustände:
    - public = von außen jederzeit erreichbar
    - protected = von außen erreichbar, aber hinweis in der IDE
    - private = nicht von außen erreichbar

    Aber selbst private bietet keinen echten zugriffsschutz, denn Python gibt Privaten attributen oder Methoden
    neue namen damit diese nicht von außen erreichbar sind, kennt man den aufbau der namnen kann man trozdem
    auf das Private attribute oder die Methode zugreifen.

    Dies möglichkeit, ein attribute oder eine methode protected oder private zu machen wird eigentlich nur als kennzeichnung
    verwendet und in den meisten fällen nutzt man nur protected um entwicklern zu sagen das es sich um ein
    geschütztes attribute oder eine geschütze methode handelt
"""


class Roboter(object):
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__r = 'S'
        self._z = 0

    def schritt(self):
        if self.__r == 'O':
            self.__x = self.__x + 1
        elif self.__r == 'S':
            self.__y = self.__y + 1
        elif self.__r == 'W':
            self.__x = self.__x - 1
        elif self.__r == 'N':
            self.__y = self.__y - 1

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getR(self):
        return self.__r

    def getZustand(self):
        return (self.__x, self.__y, self.__r)

    def setZustand(self, x, y, r):
        self.__x = x
        self.__y = y
        self.__r = r


rob = Roboter()
rob.setZustand(2, 3, 'O')
print(rob.getZustand())
rob.schritt()
rob.schritt()
print(rob.getX())
print(rob.getY())

# print(rob.__x)
rob.__x = 42
print(rob.__x)
print(rob.__dict__)
