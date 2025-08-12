from tateti import Tateti
from jugador import Jugador
from tablero import Tablero
    
def main():
    juego = Tateti()
    nombre_x=str(input("Nombre del jugador X:"))
    nombre_o=str(input("Nombre del jugador O: "))
    jugadores = Jugador(nombre_x,nombre_o)

    while True:

        print("Bienvenidos al Tateti")

        print("Tablero: ")

        for i in juego.tablero.contenedor:
            print(i)

        try:
            print(f"El turno de {juego.obtener_turno(jugadores)}:")
            fil = int(input("Ingrese fila: "))
            col = int(input("Ingrese columna: "))
            juego.ocupar_una_de_las_casillas(fil, col)
            if juego.tablero.verificar_ganador():
                print(f"¡Felicidades {juego.obtener_turno(jugadores)} !ganaste.")
                break

            if juego.tablero.empate():
                print("Empataron")
                break

            juego.cambiar_turno()
        except Exception as e:
            print(e)
        
if __name__ == '__main__':
    main()