# clases.py

class Detector:
    def __init__(self):
        pass
    
    def detectar_mutantes(self, matriz):
        """Método para detectar si hay mutantes en la matriz"""
        try:
            return self._detectar_horizontal(matriz) or self._detectar_vertical(matriz) or self._detectar_diagonal(matriz)
        except Exception as e:
            print(f"Error al detectar mutantes: {e}")
            return False

    def _detectar_horizontal(self, matriz):
        """Detecta mutantes horizontales"""
        try:
            for fila in matriz:
                if any(fila[i:i+4] == "TTTT" for i in range(len(fila) - 3)):
                    return True
            return False
        except Exception as e:
            print(f"Error al detectar mutantes horizontales: {e}")
            return False
    
    def _detectar_vertical(self, matriz):
        """Detecta mutantes verticales"""
        try:
            for col in range(len(matriz[0])):
                for row in range(len(matriz) - 3):
                    if all(matriz[row + i][col] == 'T' for i in range(4)):
                        return True
            return False
        except Exception as e:
            print(f"Error al detectar mutantes verticales: {e}")
            return False
    
    def _detectar_diagonal(self, matriz):
        """Detecta mutantes diagonales"""
        try:
            for row in range(len(matriz) - 3):
                for col in range(len(matriz[0]) - 3):
                    if all(matriz[row + i][col + i] == 'T' for i in range(4)):
                        return True
            return False
        except Exception as e:
            print(f"Error al detectar mutantes diagonales: {e}")
            return False


class Mutador:
    def __init__(self, base_nitrogenada, base_inicial, orientacion):
        self.base_nitrogenada = base_nitrogenada
        self.base_inicial = base_inicial
        self.orientacion = orientacion
    
    def crear_mutante(self):
        pass


class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, base_inicial, orientacion):
        super().__init__(base_nitrogenada, base_inicial, orientacion)
    
    def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        """Crea un mutante horizontal o vertical"""
        try:
            base = base_nitrogenada
            fila, col = posicion_inicial
            if orientacion_de_la_mutacion == 'H':
                if fila < 0 or fila >= len(matriz) or col < 0 or col + 3 >= len(matriz[0]):
                    raise ValueError("Posición fuera de rango para la mutación horizontal.")
                for i in range(4):
                    matriz[fila][col + i] = base
            elif orientacion_de_la_mutacion == 'V':
                if fila < 0 or fila + 3 >= len(matriz) or col < 0 or col >= len(matriz[0]):
                    raise ValueError("Posición fuera de rango para la mutación vertical.")
                for i in range(4):
                    matriz[fila + i][col] = base
            else:
                raise ValueError("La orientación debe ser 'H' o 'V'.")
            return matriz
        except ValueError as e:
            print(f"Error en la mutación: {e}")
            return matriz
        except IndexError as e:
            print(f"Error de índice en la mutación: {e}")
            return matriz
        except Exception as e:
            print(f"Error inesperado en la mutación: {e}")
            return matriz


class Virus(Mutador):
    def __init__(self, base_nitrogenada, base_inicial, orientacion):
        super().__init__(base_nitrogenada, base_inicial, orientacion)
    
    def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial):
        """Crea un mutante diagonal"""
        try:
            base = base_nitrogenada
            fila, col = posicion_inicial
            if fila < 0 or fila + 3 >= len(matriz) or col < 0 or col + 3 >= len(matriz[0]):
                raise ValueError("Posición fuera de rango para la mutación diagonal.")
            for i in range(4):
                matriz[fila + i][col + i] = base
            return matriz
        except ValueError as e:
            print(f"Error en la mutación: {e}")
            return matriz
        except IndexError as e:
            print(f"Error de índice en la mutación: {e}")
            return matriz
        except Exception as e:
            print(f"Error inesperado en la mutación: {e}")
            return matriz


class Sanador:
    def __init__(self):
        pass
    
    def sanar_mutantes(self, matriz):
        """Sanar cualquier mutación detectada"""
        try:
            detector = Detector()
            if detector.detectar_mutantes(matriz):
                return self._generar_nuevo_adn()
            return matriz
        except Exception as e:
            print(f"Error al intentar sanar el ADN: {e}")
            return matriz
    
    def _generar_nuevo_adn(self):
        """Genera un ADN sin mutaciones"""
        try:
            import random
            bases = ['A', 'T', 'C', 'G']
            return ["".join(random.choice(bases) for _ in range(6)) for _ in range(6)]
        except Exception as e:
            print(f"Error al generar un nuevo ADN: {e}")
            return []
