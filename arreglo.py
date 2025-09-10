import random

# Arreglo de 10 enteros aleatorios (1..100)
arreglo = [random.randint(1, 100) for _ in range(10)]

print("Arreglo creado:", arreglo)

# recorrido usando for clásico usando índices
print("\nFor clásico:")
for i in range(len(arreglo)):
    print(f"Índice {i}: {arreglo[i]}")

# recirrido usando for-each
print("\nFor-each:")
for valor in arreglo:
    print(f"Valor: {valor}")

# modificacion
for i in range(len(arreglo)):
    if arreglo[i] % 2 != 0:
        arreglo[i] = 0
    arreglo[i] *= i

# bucle
def busqueda_lineal(arr, valor):
    for i in range(len(arr)):
        if arr[i] == valor:
            return i
    return -1

print("Resultado búsqueda:", busqueda_lineal(arreglo, 50))
