from Negocio.Partida import Partida
from Negocio.jugador import Jugador

class Pirinola:
    def __init__(self,nombre_piri,id_partida,valor_partida):
        self.nombre_piri=nombre_piri
        self.partida = Partida(id_partida,valor_partida)

    def iniciar_juego(self):
        self.numero_jugadores=int(input("Digite numero Jugadores"))
        nu=0
        while( nu < self.numero_jugadores):
            nombre=input("Digite nombre Jugador")
            plante = input("Digite plante del Jugador")
            self.partida.add_jugador(nombre,plante)
            nu=nu+1