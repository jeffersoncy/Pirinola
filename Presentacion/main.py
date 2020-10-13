# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Negocio.Pirinola import Pirinola

opc = 0

while opc != 4:
    if opc == 1:
        print("JUGAR NUEVA PARTIDA")
        id_partida = input("Ingrese el id de la Partida: ")
        val_Partida = int(input("Ingrese el valor de la Partida: "))
        piri = Pirinola("Juanito",id_partida,val_Partida)
        #piri = Pirinola("Piri de Juan", 1, 2000)

        piri.iniciar_juego()
        piri.partida.inicia_turnos()
        part = piri.partida
        piri.add_partida(part)

    if opc == 2:
        print("IMPRIMIR LISTA DE PARTIDAS")

        for k in piri.ListPartidas:
            print("ID Partida: " + k.id_partida)
            print("Valor Partida: ", k.valor_partida)
            print("Jugador Ganador: " + k.Jugador_Ganador)
            print("Valor Ganado: ",k.Valor_Total_Ganado)

    if opc == 3:
        print("NO SE SABE")

    print("------------------------MENU PRINCIPAL-----------------------")
    print("1. Jugar partida")
    print("2. Lista de partidas")
    print("3. no se sabe")
    print("4. Salir")
    print("-------------------------------------------------------------")

    opc = input("Digite una opcion: ")
    if opc.isdigit() == True:
        opc = int(opc)