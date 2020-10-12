# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Negocio.Pirinola import Pirinola

piri= Pirinola("Piri de Juan",1,2000)
piri.iniciar_juego()
#print(piri.partida.calcular_acumulado_inicial())
piri.partida.inicia_turnos()
print(piri.partida.acumulado)
#print(piri.partida.calcular_acumulado_inicial())