from Negocio.jugador import Jugador
from random import randint

class Turno:
    def __init__(self,jugador,id_turno,valor_plante):
        self.jugador=Jugador(jugador,valor_plante)
        self.id_turno=id_turno
        self.valor_sacado = self.retornar_valor_sacado()

    def retornar_valor_sacado(self):
        valores=['Toma1','Toma2','Pon1','Pon2','TodosPonen','TomaTodo']
        valor_opcion = randint(0,5)
        return valores[valor_opcion]