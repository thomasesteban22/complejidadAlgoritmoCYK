
import time
import matplotlib.pyplot as plt

# Función del algoritmo CYK
def analizar_cyk(gramatica, cadena):
    n = len(cadena)
    r = len(gramatica)
    
    # Inicializa la tabla de CYK
    tabla = [[set() for _ in range(n)] for _ in range(n)]
    
    # Rellena la tabla con producciones unitarias
    for i, ch in enumerate(cadena):
        for izq, der in gramatica:
            if der == ch:
                tabla[i][i].add(izq)
    
    # Aplica las producciones binarias
    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            for k in range(i, j):
                for izq, der in gramatica:
                    if len(der) == 2 and der[0] in tabla[i][k] and der[1] in tabla[k + 1][j]:
                        tabla[i][j].add(izq)
    
    # La cadena es aceptada si el símbolo inicial S está en la celda (0, n-1)
    return 'S' in tabla[0][n - 1]

# Medir el tiempo de ejecución para diferentes tamaños de cadena
def medir_tiempos(gramatica, cadenas):
    tiempos = []
    for cadena in cadenas:
        inicio = time.time()
        analizar_cyk(gramatica, cadena)
        fin = time.time()
        tiempos.append(fin - inicio)
    return tiempos

# Ejemplo de gramática en FNC
gramatica = [
    ('S', 'AB'), ('S', 'BC'),
    ('A', 'a'), ('B', 'b'), ('C', 'c'),
    ('A', 'AA'), ('B', 'BB'), ('C', 'CC')
]

# Generar cadenas de prueba con una cadena bastante larga
cadenas_prueba = [
    "a", "ab", "abc", "abbc", "aabbc", "aaabbcc", "aaaabbbbcccc",
    "a" * 50 + "b" * 50, "a" * 100 + "b" * 100, "a" * 200 + "b" * 200
]

# Medir tiempos de ejecución para cada cadena
tiempos = medir_tiempos(gramatica, cadenas_prueba)

# Graficar el tiempo de ejecución en función de la longitud de la cadena
longitudes = [len(cadena) for cadena in cadenas_prueba]
plt.plot(longitudes, tiempos, marker='o')
plt.xlabel('Longitud de la cadena')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución del Algoritmo CYK')
plt.grid(True)
plt.show()
