import random
import bisect 


# Busqueda lineal
def busqueda_lineal(lista, clave):
    for i, valor in enumerate(lista):
        if valor == clave:
            return i
    return -1

# Busqueda binaria 
def busqueda_binaria(lista, clave):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == clave:
            return medio
        elif lista[medio] < clave:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Algoritmos de ordenamiento manuales


def ordenamiento_burbuja(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenamiento_insercion(lista):
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + centro + quicksort(derecha)

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Juego del ahorcado
def obtener_palabra_aleatoria():
    palabras = ["materia", "comida", "agua", "gato", "felicidad", "saltar", "futbol"]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra
        else:
            tablero += "_"
    print(tablero)

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos_restantes = 10

    # Lista ordenada de letras unicas
    letras_ordenadas = sorted(set(palabra_secreta))

    print("\n JUEGO DEL AHORCADO CON ALGORITMOS DE BUSQUEDA \n")
    while intentos_restantes > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra = input("Escribe una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has ingresado esta letra cachon, intenta con otra.\n")
            continue

        # Verificacion con busqueda lineal
        pos_lineal = busqueda_lineal(list(palabra_secreta), letra)

        # Verificacion con busqueda binaria
        pos_binaria = busqueda_binaria(letras_ordenadas, letra)

        if pos_lineal != -1:
            letras_adivinadas.append(letra)
            print(f"La letra '{letra}' encontrada con búsqueda lineal en posición {pos_lineal}.")
            print(f"También comprobada con búsqueda binaria: índice {pos_binaria} en lista ordenada.\n")

            if set(palabra_secreta).issubset(set(letras_adivinadas)):
                print(f"Felicidades heyy, eres la patada, adivinaste la palabra: {palabra_secreta}")
                break
        else:
            intentos_restantes -= 1
            print(f"La letra '{letra}' no esta cachon. Ya te quedan {intentos_restantes} intentos.\n")

    if intentos_restantes == 0:
        print(f"Has perdido, no te dio el coco para adivinar esta palabra: {palabra_secreta}")

    # Demostracion de ordenamientos
    print("\n DEMOSTRACIÓN DE ORDENAMIENTOS ")
    numeros = [random.randint(0, 99) for _ in range(10)]
    print("Lista original:", numeros)

    print("Burbuja:", ordenamiento_burbuja(numeros))
    print("Insercion:", ordenamiento_insercion(numeros))
    print("Quicksort:", quicksort(numeros))
    print("Mergesort:", mergesort(numeros))

    # Metodos nativos de Python
    print("\n METODOS NATIVOS DE PYTHON ")
    print("Ordenamiento con sorted():", sorted(numeros))
    lista_copia = numeros.copy()
    lista_copia.sort()
    print("Ordenamiento con .sort():", lista_copia)
    clave = lista_copia[3]
    print(f"Clave a buscar: {clave}")
    print("¿Esta en la lista? (in):", clave in lista_copia)
    pos_bisect = bisect.bisect_left(lista_copia, clave)
    print(f"Posicion con bisect (búsqueda binaria): {pos_bisect}\n")


jugar_ahorcado()
