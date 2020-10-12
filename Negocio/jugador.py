class Jugador:
    def __init__(self,nombre,plante):
        self.nombre_jugador = nombre
        self.plante = plante

    def get_nombre(self):
        return self.nombre_jugador

    def get_plante(self):
        return self.plante

    def set_plante(self,new_valor):
        self.plante = new_valor
