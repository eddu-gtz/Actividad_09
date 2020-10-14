from particula import Particula

class Administradora:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

lista = Administradora()
p01 = Particula(1, 7, 5, 4, 1, 500, 255, 255, 125)
p02 = Particula(2, 100, 200, 200, 1, 430, 25, 125, 125)
lista.agregar_final(p01)
lista.agregar_inicio(p02)
lista.mostrar()