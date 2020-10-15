"""Presentado por :  Danny Alberto Días Mage
                     Jefferson Eduardo Campo Yule"""
from Negocio.Pirinola import Pirinola
bandera = False
opc = 0
varAuto = 1
while opc != 5:
    if opc == 1:
        print("JUGAR NUEVA PARTIDA")
        print("Es necesario que los jugadores o participantes")
        print("tengan un mismo plante para poder jugar")
        val_Partida = int(input("Ingrese el valor de la Partida: "))
        piri = Pirinola("Juanito",varAuto,val_Partida)
        piri.iniciar_juego()
        piri.partida.inicia_turnos()
        part = piri.partida
        piri.add_partida(part)
        varAuto = varAuto + 1
        bandera = True

    if opc == 2:
        print("IMPRIMIR LISTA DE PARTIDAS")
        if(bandera == True):
            if len(piri.ListPartidas) != 0:

                for k in piri.ListPartidas:
                    print("------------------------------------------------------")
                    print("ID Partida: ", k.id_partida)
                    print("Valor Partida: ", k.valor_partida)
                    print("Jugador Ganador: " + k.Jugador_Ganador)
                    print("Valor Ganado: ", k.Valor_Total_Ganado)
                    print("------------------------------------------------------")
            else:
                print("SIN PARTIDAS")
        else:
            print("SIN PARTIDAS")
    if opc == 3:
        print("BUSCAR PARTIDA")
        if(bandera == True):
            bus_id = int(input("Ingrese el ID de la partida que desea buscar: "))
            bus_validar = False
            bus_indice = 0
            bus_reIndice = 0
            for n in piri.ListPartidas:
                bus_id_actual = getattr(n, "id_partida")
                if (bus_id_actual == bus_id):
                    bus_validar = True
                    bus_reIndice = bus_indice
                    break
                bus_indice = bus_indice + 1
            if (bus_validar == True):
                print("ID de la partida: ", piri.ListPartidas[bus_reIndice].id_partida)
                print("Valor de la Partida: ", piri.ListPartidas[bus_reIndice].valor_partida)
                print("Jugador Ganador: ", piri.ListPartidas[bus_reIndice].Jugador_Ganador)
                print("Valor Ganado", piri.ListPartidas[bus_reIndice].Valor_Total_Ganado)
            else:
                print("El ID ingresado no ha sido encontrado")
        else:
            print("SIN PARTIDAS")

    if opc == 4:
        print("REINICIAR PARTIDAS")
        if(bandera == True):
            piri.ListPartidas.clear()
            print("Partidas reiniciadas")
        else:
            print("SIN PARTIDAS")

    print("------------------------MENU PRINCIPAL-----------------------")
    print("1. Jugar partida")
    print("2. Lista de partidas")
    print("3. Buscar partida")
    print("4. Reiniciar partidas")
    print("5. Salir")
    print("-------------------------------------------------------------")

    opc = input("Digite una opcion: ")
    if opc.isdigit() == True:
        opc = int(opc)