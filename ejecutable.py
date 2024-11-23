# ejecutable.py
from clases import Detector, Radiacion, Virus, Sanador

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Detectar mutaciones")
    print("2. Mutar ADN")
    print("3. Sanar ADN")
    print("4. Salir")

def pedir_adn():
    matriz = []
    print("Ingrese la secuencia de ADN de 6x6 (una fila por vez, sin espacios):")
    for i in range(6):
        while True:
            try:
                fila = input(f"Fila {i + 1}: ")
                if len(fila) != 6:
                    raise ValueError("Cada fila debe tener exactamente 6 caracteres.")
                if not all(c in 'ATCG' for c in fila):
                    raise ValueError("La fila debe contener solo las bases A, T, C y G.")
                matriz.append(fila)
                break
            except ValueError as e:
                print(f"Error: {e}")
    return matriz

def main():
    while True:
        mostrar_menu()
        opcion = input("Opción: ")
        
        if opcion == "1":
            try:
                matriz = pedir_adn()
                detector = Detector()
                if detector.detectar_mutantes(matriz):
                    print("¡El ADN es un mutante!")
                else:
                    print("El ADN no tiene mutaciones.")
            except Exception as e:
                print(f"Error al ejecutar la detección de mutantes: {e}")
        
        elif opcion == "2":
            try:
                matriz = pedir_adn()
                base = input("Base nitrogenada a mutar (A, T, C, G): ")
                if base not in "ATCG":
                    raise ValueError("Base nitrogenada inválida. Debe ser A, T, C o G.")
                posicion = tuple(map(int, input("Posición inicial (fila, columna): ").split(',')))
                if len(posicion) != 2 or not all(0 <= p < 6 for p in posicion):
                    raise ValueError("Posición inicial inválida. Debe ser una tupla de dos enteros entre 0 y 5.")
                orientacion = input("Orientación de la mutación (H para horizontal, V para vertical): ").upper()
                if orientacion not in ['H', 'V']:
                    raise ValueError("Orientación inválida. Debe ser 'H' o 'V'.")
                
                radiacion = Radiacion(base, posicion, orientacion)
                matriz_mutada = radiacion.crear_mutante(matriz, base, posicion, orientacion)
                print("ADN mutado:")
                for fila in matriz_mutada:
                    print(fila)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error al intentar mutar el ADN: {e}")
        
        elif opcion == "3":
            try:
                matriz = pedir_adn()
                sanador = Sanador()
                matriz_sanada = sanador.sanar_mutantes(matriz)
                print("ADN sanado:")
                for fila in matriz_sanada:
                    print(fila)
            except Exception as e:
                print(f"Error al intentar sanar el ADN: {e}")
        
        elif opcion == "4":
            print("Saliendo...")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
