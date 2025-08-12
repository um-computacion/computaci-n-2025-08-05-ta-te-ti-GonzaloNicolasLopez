import unittest
from tateti import Tateti
from jugador import Jugador
from tablero import Tablero, PosOcupadaException

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.juego = Tateti()
        self.jugadores = Jugador("sanchi", "gonzalo")

    
    def test_crear_jugador(self):
        jugador = self.juego.crear_jugador("sanchi", "gonzalo")
        self.assertEqual(jugador.jugador_x, "sanchi")
        self.assertEqual(jugador.jugador_o, "gonzalo")

    
    def test_turno_inicial(self):
        self.assertEqual(self.juego.turno, "X")

    
    def test_cambiar_turno_a_o(self):
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.turno, "O")

    def test_cambiar_turno_a_x(self):
        self.juego.turno = "O"
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.turno, "X")

    
    def test_ocupar_casilla_vacia(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.tablero.contenedor[0][0], "X")

    
    def test_ocupar_casilla_ocupada(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_una_de_las_casillas(0, 0)

    
    def test_ganador_fila(self):
        tablero = self.juego.tablero
        tablero.contenedor = [["X", "X", "X"],
                              ["", "", ""],
                              ["", "", ""]]
        self.assertTrue(tablero.verificar_ganador())

    
    def test_ganador_columna(self):
        tablero = self.juego.tablero
        tablero.contenedor = [["O", "", ""],
                              ["O", "", ""],
                              ["O", "", ""]]
        self.assertTrue(tablero.verificar_ganador())

    
    def test_ganador_diagonal_principal(self):
        tablero = self.juego.tablero
        tablero.contenedor = [["X", "", ""],
                              ["", "X", ""],
                              ["", "", "X"]]
        self.assertTrue(tablero.verificar_ganador())


    def test_ganador_diagonal_inversa(self):
        tablero = self.juego.tablero
        tablero.contenedor = [["", "", "O"],
                              ["", "O", ""],
                              ["O", "", ""]]
        self.assertTrue(tablero.verificar_ganador())

    
    def test_empate(self):
        tablero = self.juego.tablero
        tablero.contenedor = [["X", "O", "X"],
                              ["X", "O", "O"],
                              ["O", "X", "X"]]
        self.assertTrue(tablero.empate())

    def test_no_empate_si_hay_espacio(self):
        tablero = self.juego.tablero
        tablero.contenedor = [["X", "O", ""],
                              ["X", "O", "O"],
                              ["O", "X", "X"]]
        self.assertFalse(tablero.empate())

    
    def test_obtener_turno(self):
        self.assertEqual(self.juego.obtener_turno(self.jugadores), "sanchi(X)")
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.obtener_turno(self.jugadores), "gonzalo(O)")

if __name__ == "__main__":
    unittest.main()
