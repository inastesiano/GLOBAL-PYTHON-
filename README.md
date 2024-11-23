# Instructivo para la ejecución del programa de detección de mutaciones en ADN

Este programa simula un sistema para detectar y mutar secuencias de ADN, identificando posibles mutaciones horizontales, verticales o diagonales en una matriz 6x6 que representa el ADN. Además, incluye la capacidad de sanar las mutaciones generando un nuevo ADN sin mutaciones.


## Archivos incluidos en el repositorio

- **clases.py**: Define las clases `Detector`, `Mutador`, `Radiacion`, `Virus`, y `Sanador`, que se encargan de detectar mutaciones, crear mutantes y sanar el ADN.
- **ejecutable.py**: Archivo principal que se ejecuta para interactuar con el usuario, permitiendo elegir entre detectar mutaciones, mutar el ADN o sanarlo.
- **README.txt**: Este archivo, que proporciona instrucciones sobre cómo ejecutar el programa.

## Ejecución del programa

Para ejecutar el programa, sigue estos pasos:

1. Abre una terminal o línea de comandos en tu computadora.
2. Navega a la carpeta que contiene los archivos `clases.py` y `ejecutable.py`.
3. Ejecuta el archivo `ejecutable.py` usando Python. En la terminal, escribe el siguiente comando:


Esto iniciará el programa y verás un menú con las siguientes opciones:

1. **Detectar mutaciones**: Te pedirá ingresar una secuencia de ADN (6 filas, 6 caracteres por fila). El programa verificará si hay alguna mutación en la secuencia (horizontales, verticales o diagonales).
2. **Mutar ADN**: Te permitirá ingresar una secuencia de ADN y realizar una mutación en una base nitrogenada específica, en una posición dada y en una orientación definida (horizontal o vertical).
3. **Sanar ADN**: Si el ADN contiene mutaciones, el programa generará un ADN completamente nuevo sin mutaciones y lo mostrará.
4. **Salir**: Termina la ejecución del programa.


"# GLOBAL-PYTHON-" 
