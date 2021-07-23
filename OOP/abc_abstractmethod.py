"""
    Wie wir wissen bestehen methoden aus einem namen, kann parameter annehmen und besteht aus einem Body
    in dem wir rechechnungen oder aktionen durchführen können.
    Aber was wenn wir nicht mit der Methode tun möchten ?
    Wir könnten in den Methoden körper ein "pass" schreiben, aber das würde uns ggf. zu fehlern führen wenn
    wir wollten das die Methode von einer anderen Klasse implementiert werden muss und wir dort
    die implementierung des body vornehmen.
"""
from abc import ABC, abstractmethod


class Computer:
    def process(self):
        print("Running Process")


class Computer:
    def process(self):
        pass


computer1 = Computer()
computer1.process()


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("running process")


class MobilePhone(Computer):
    def process(self):
        print("running process")


# class Paper(Computer):
#     def write(self):
#         print("writing")

class Programmer:
    def work(self, computer):
        print("Solving Bugs")
        computer.process()


laptop = Laptop()

programmer = Programmer()
programmer.work(laptop)

"""
    
"""
