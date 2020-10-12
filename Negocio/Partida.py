from Negocio.Turno import Turno
from Negocio.jugador import Jugador

class Partida:
    def __init__(self, id_partida, valor_partida):
        self.id_partida = id_partida
        self.valor_partida = valor_partida
        self.lista_jugadores = list()
        self.lista_turnos = list()
        self.acumulado = self.calcular_acumulado_inicial()


    def add_jugador(self, nombre, valor_plante):
        self.lista_jugadores.append(Jugador(nombre,valor_plante))


    def listar_jugadores(self):
        for juga in self.lista_jugadores:
            dato = getattr(juga, 'nombre_jugador')
            dato2 = getattr(juga, 'plante')
            print(dato)
            print(dato2)

    def calcular_acumulado_inicial(self):
        valor = self.valor_partida * len(self.lista_jugadores)
        return valor


    #def calcular_acumulado_turno(self):
        #valor = self.valor_partida * len(self.lista_jugadores)
        #return valor


    def add_turno(self, jugador, id_turno):
        self.lista_turnos.append(Turno(jugador, id_turno))

    def inicia_turnos(self):
        resultado_turno = ''
        n_jugador = 0
        n_turno = 0
        self.acumulado = self.valor_partida * len(self.lista_jugadores)
        while (resultado_turno != 'TomaTodo'):
            print("Lanza jugador", self.lista_jugadores[n_jugador].get_nombre(), ", Plante: ", self.lista_jugadores[n_jugador].get_plante())
            self.lista_turnos.append(Turno(self.lista_jugadores[n_jugador].get_nombre(), n_turno, self.lista_jugadores[n_jugador].get_plante()))
            resultado_turno = self.lista_turnos[n_turno].retornar_valor_sacado()
            print("Valor ", resultado_turno, 'Turno', n_turno)
            if resultado_turno == 'Toma1':
                self.acumulado = self.acumulado - self.valor_partida
                valor = self.lista_jugadores[n_jugador].get_plante() + self.valor_partida
                self.lista_jugadores[n_jugador].set_plante(valor)
            elif resultado_turno == 'Toma2':
                self.acumulado = self.acumulado - (2 * self.valor_partida)
                valor = self.lista_jugadores[n_jugador].get_plante() + (2 * self.valor_partida)
                self.lista_jugadores[n_jugador].set_plante(valor)
            elif resultado_turno == 'Pon2':
                self.acumulado = self.acumulado + (2 * self.valor_partida)
                valor = self.lista_jugadores[n_jugador].get_plante() - (2 * self.valor_partida)
                self.lista_jugadores[n_jugador].set_plante(valor)
            elif resultado_turno == 'Pon1':
                self.acumulado = self.acumulado + self.valor_partida
                valor = self.lista_jugadores[n_jugador].get_plante() - self.valor_partida
                self.lista_jugadores[n_jugador].set_plante(valor)
            elif resultado_turno == 'TodosPonen':
                self.acumulado = self.acumulado + (self.valor_partida * len(self.lista_jugadores))
                for i in self.lista_jugadores:
                    valor = i.get_plante() - self.valor_partida
                    i.set_plante(valor)
            elif resultado_turno == 'TomaTodo':
                valor = self.lista_jugadores[n_jugador].get_plante() + (self.acumulado)
                self.lista_jugadores[n_jugador].set_plante(valor)
                self.acumulado = 0
            print("Acumulado por Turno: ", self.acumulado)
            print(self.lista_jugadores[n_jugador].get_plante())
            print("------------------------------------------------------------")
            n_turno = n_turno + 1
            n_jugador = n_jugador + 1
            if (n_jugador == len(self.lista_jugadores)):
                n_jugador = 0
            #os.system('pause')