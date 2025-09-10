import random

def obtener_palabra_aleatoria():
    palabras = ["materia", "comida", "agua", "gato", "felicidad", "saltar", "futbol"]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria   # 👈 aquí faltaba devolver la palabra

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
    
    while intentos_restantes > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra = input("👉 Introduce una letra: ").lower()
        
        if letra in letras_adivinadas:  
            print(" Ya has ingresado esta letra, intenta con otra. ")
            continue
        
        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            # Aquí verificamos si ya adivinó todas las letras
            if set(palabra_secreta).issubset(set(letras_adivinadas)):
                print(f" Felicidades, adivinaste la palabra: {palabra_secreta}")
                break            
        else:
            intentos_restantes -= 1
            print(f" La letra es incorrecta, te quedan {intentos_restantes} intentos.")
    
    if intentos_restantes == 0:
        print(f" Has perdido, la palabra secreta era: {palabra_secreta}")
        
jugar_ahorcado()
