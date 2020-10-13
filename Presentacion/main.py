# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Negocio.Pirinola import Pirinola

opc = 0
varAuto = 1
while opc != 4:
    if opc == 1:
        print("JUGAR NUEVA PARTIDA")
        #id_partida = input("Ingrese el id de la Partida: ")
        val_Partida = int(input("Ingrese el valor de la Partida: "))
        piri = Pirinola("Juanito",varAuto,val_Partida)
        #piri = Pirinola("Piri de Juan", 1, 2000)

        piri.iniciar_juego()
        piri.partida.inicia_turnos()
        part = piri.partida
        piri.add_partida(part)
        varAuto = varAuto + 1

    if opc == 2:
        print("IMPRIMIR LISTA DE PARTIDAS")

        for k in piri.ListPartidas:
            print("------------------------------------------------------")
            print("ID Partida: ", k.id_partida)
            print("Valor Partida: ", k.valor_partida)
            print("Jugador Ganador: " + k.Jugador_Ganador)
            print("Valor Ganado: ",k.Valor_Total_Ganado)
            print("------------------------------------------------------")

    if opc == 3:
        print("BUSCAR PARTIDA")
        bus_id = int(input("Ingrese el ID de la partida que desea buscar: "))
        bus_validar = False
        bus_indice = 0
        bus_reIndice = 0
        for n in piri.ListPartidas:
            bus_id_actual = getattr(n,"id_partida")
            if(bus_id_actual == bus_id):
                bus_validar = True
                bus_reIndice = bus_indice
                break
            bus_indice = bus_indice + 1
        if(bus_validar == True):
            print("ID de la partida: ",piri.ListPartidas[bus_reIndice].id_partida)
            print("Valor de la Partida: ", piri.ListPartidas[bus_reIndice].valor_partida)
            print("Jugador Ganador: ", piri.ListPartidas[bus_reIndice].Jugador_Ganador)
            print("Valor Ganado",piri.ListPartidas[bus_reIndice].Valor_Total_Ganado)
        else:
            print("El ID ingresado no ha sido encontrado")

    print("------------------------MENU PRINCIPAL-----------------------")
    print("1. Jugar partida")
    print("2. Lista de partidas")
    print("3. Buscar partida")
    print("4. Salir")
    print("-------------------------------------------------------------")

    opc = input("Digite una opcion: ")
    if opc.isdigit() == True:
        opc = int(opc)