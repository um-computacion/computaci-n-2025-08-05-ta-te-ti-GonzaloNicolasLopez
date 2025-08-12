from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()

    def crear_jugador(self,nombre_x,nombre_o):
        return Jugador(nombre_x,nombre_o)

    def ocupar_una_de_las_casillas(self, fil, col):
        self.tablero.poner_la_ficha(fil, col, self.turno)

    def cambiar_turno(self):
        if self.turno == "X":
            self.turno = "O"
        else:
            self.turno = "X"

    def obtener_turno(self,jugadores):

        if self.turno == "X":
            return f"{jugadores.jugador_x}(X)"

        else:
            return f"{jugadores.jugador_o}(O)"
