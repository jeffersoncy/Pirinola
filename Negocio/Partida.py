"""Presentado por :  Danny Alberto Días Mage
                     Jefferson Eduardo Campo Yule"""
from Negocio.Turno import Turno
from Negocio.jugador import Jugador
import os

class Partida:
    def __init__(self, id_partida, valor_partida):
        self.id_partida = id_partida
        self.valor_partida = valor_partida
        self.lista_jugadores = list()
        self.lista_turnos = list()
        self.Jugador_Ganador = 0
        self.Turno_Ganador = 0
        self.Valor_Total_Ganado = 0
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

    def add_turno(self, jugador, id_turno):
        self.lista_turnos.append(Turno(jugador, id_turno))

    def inicia_turnos(self):
        resultado_turno = ''
        n_jugador = 0
        n_turno = 0
        self.acumulado = self.valor_partida * len(self.lista_jugadores)
        print("------------------------------------------------------------")
        while self.acumulado != 0:
            print("Lanza jugador", self.lista_jugadores[n_jugador].get_nombre(), ", Plante Actual: ", self.lista_jugadores[n_jugador].get_plante())
            self.lista_turnos.append(Turno(self.lista_jugadores[n_jugador].get_nombre(), n_turno, self.lista_jugadores[n_jugador].get_plante()))
            resultado_turno = self.lista_turnos[n_turno].retornar_valor_sacado()
            print("Valor ", resultado_turno, 'Turno', n_turno)
            if resultado_turno == 'Toma1':
                self.acumulado = self.acumulado - self.valor_partida
                if self.acumulado >= 0:
                    valor = self.lista_jugadores[n_jugador].get_plante() + self.valor_partida
                    self.lista_jugadores[n_jugador].set_plante(valor)
                else:
                    self.acumulado = 0
            elif resultado_turno == 'Toma2':
                self.acumulado = self.acumulado - (2 * self.valor_partida)
                if self.acumulado >= 0:
                    valor = self.lista_jugadores[n_jugador].get_plante() + (2 * self.valor_partida)
                    self.lista_jugadores[n_jugador].set_plante(valor)
                else:
                    self.acumulado = 0
            elif resultado_turno == 'Pon2':
                if self.lista_jugadores[n_jugador].get_plante() >= (self.valor_partida*2):
                    self.acumulado = self.acumulado + (2 * self.valor_partida)
                    valor = self.lista_jugadores[n_jugador].get_plante() - (2 * self.valor_partida)
                    self.lista_jugadores[n_jugador].set_plante(valor)
                else:
                    self.lista_jugadores[n_jugador].set_plante(0)
            elif resultado_turno == 'Pon1':
                if self.lista_jugadores[n_jugador].get_plante() >= self.valor_partida:
                    self.acumulado = self.acumulado + self.valor_partida
                    valor = self.lista_jugadores[n_jugador].get_plante() - self.valor_partida
                    self.lista_jugadores[n_jugador].set_plante(valor)
                else:
                    self.lista_jugadores[n_jugador].set_plante(0)
            elif resultado_turno == 'TodosPonen':
                acumulado = 0
                for i in self.lista_jugadores:
                    valor = i.get_plante() - self.valor_partida
                    if(valor >= 0):
                        acumulado = acumulado + self.valor_partida
                        i.set_plante(valor)
                self.acumulado = self.acumulado + acumulado
            elif resultado_turno == 'TomaTodo':
                valor = self.lista_jugadores[n_jugador].get_plante() + (self.acumulado)
                self.lista_jugadores[n_jugador].set_plante(valor)
                self.acumulado = 0
            print("Acumulado por Turno: ", self.acumulado)
            if self.lista_jugadores[n_jugador].get_plante() > 0:
                print("Nuevo Plante: ",self.lista_jugadores[n_jugador].get_plante())
            else:
                print("Juego Terminado para ",self.lista_jugadores[n_jugador].get_nombre(),", sin plante para continuar")
                self.lista_jugadores.pop(n_jugador)
                n_jugador = n_jugador - 1

            print("------------------------------------------------------------")
            n_turno = n_turno + 1
            n_jugador = n_jugador + 1
            if (n_jugador == len(self.lista_jugadores)):
                n_jugador = 0
            if self.acumulado == 0:
                encontrar = 0
                ganador = 0
                for i in self.lista_jugadores:
                    if i.get_plante() > encontrar:
                        encontrar = i.get_plante()
                        ganador = self.lista_jugadores.index(i)
                self.Jugador_Ganador = self.lista_jugadores[ganador].get_nombre()
                self.Turno_Ganador = n_turno
                self.Valor_Total_Ganado = self.lista_jugadores[ganador].get_plante()
                print("------------------------------------------------------------")
                print("Jugador Ganador")
                print("Valor de la Partida: ",self.valor_partida)
                print("Jugador Ganador: ",self.Jugador_Ganador)
                print("Valor Ganado",self.Valor_Total_Ganado)
            elif len(self.lista_jugadores) == 1:
                if(self.lista_jugadores[0].get_plante()==0):
                    print("------------------------------------------------------------")
                    print("Empate")
                    self.Jugador_Ganador = "Ninguno"
                    self.Turno_Ganador = n_turno
                    self.Valor_Total_Ganado = "0"
                    print("------------------------------------------------------------")
                    print("Jugador Ganador")
                    print("Valor de la Partida: ", self.valor_partida)
                    print("Jugador Ganador: ", self.Jugador_Ganador)
                    print("Valor Ganado", self.Valor_Total_Ganado)
                    self.acumulado = 0
                else:
                    self.Jugador_Ganador = self.lista_jugadores[0].get_nombre()
                    self.Turno_Ganador = n_turno
                    self.Valor_Total_Ganado = self.lista_jugadores[0].get_plante()
                    print("------------------------------------------------------------")
                    print("Jugador Ganador")
                    print("Valor de la Partida: ", self.valor_partida)
                    print("Jugador Ganador: ", self.Jugador_Ganador)
                    print("Valor Ganado", self.Valor_Total_Ganado)
                    self.acumulado = 0
            os.system('pause')