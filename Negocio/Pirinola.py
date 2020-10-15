"""Presentado por :  Danny Alberto Días Mage
                     Jefferson Eduardo Campo Yule"""
from Negocio.Partida import Partida

class Pirinola:
    ListPartidas = list()
    def __init__(self,nombre_piri,id_partida,valor_partida):
        self.nombre_piri=nombre_piri
        self.partida = Partida(id_partida,valor_partida)


    def add_partida(self, prmPartida):
        self.ListPartidas.append(prmPartida)

    def iniciar_juego(self):
        self.numero_jugadores=int(input("Digite numero Jugadores"))
        nu=0
        while( nu < self.numero_jugadores):
            nombre=input("Digite nombre Jugador")
            plante = int(input("Digite plante del Jugador"))

            if(nu == 0):
                while(plante < self.partida.valor_partida):
                    plante = int(input("Digite plante del Jugador"))
                valor = plante

            while(plante < self.partida.valor_partida or valor != plante):
                if(plante < self.partida.valor_partida):
                    print("El plnate debe ser mayor al valor de la partida ")
                else:
                    print("El plante debe ser el mismo para los participantes")
                plante = int(input("Digite plante del Jugador"))
            self.partida.add_jugador(nombre,plante)
            nu=nu+1