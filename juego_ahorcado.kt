import kotlin.random.Random

fun obtenerPalabraAleatoria(): String {
    val palabras = listOf("materia", "comida", "agua", "gato", "felicidad", "saltar", "futbol")
    return palabras.random()
}

fun mostrarTablero(palabraSecreta: String, letrasAdivinadas: Set<Char>) {
    val tablero = buildString {
        for (c in palabraSecreta) {
            append(if (c in letrasAdivinadas) c else '_')
        }
    }
    println(tablero)
}

fun jugarAhorcado() {
    val palabraSecreta = obtenerPalabraAleatoria()
    val letrasAdivinadas = mutableSetOf<Char>()
    var intentosRestantes = 10

    println("=== Juego del Ahorcado ===")
    println("La palabra tiene ${palabraSecreta.length} letras.")

    while (intentosRestantes > 0) {
        mostrarTablero(palabraSecreta, letrasAdivinadas)
        print(" Introduce una letra: ")
        val entrada = readLine()?.lowercase()

        if (entrada.isNullOrEmpty()) {
            println("Por favor escribe una letra válida.")
            continue
        }

        // Tomamos solo la primera tecla/char ingresada
        val letra = entrada[0]
        if (letra in letrasAdivinadas) {
            println(" Ya has ingresado esta letra lentejaa, intenta con otra. ")
            continue
        }

        if (letra in palabraSecreta) {
            letrasAdivinadas.add(letra)
            if (palabraSecreta.all { it in letrasAdivinadas }) {
                println(" Felicidades, sirve para algo, adivinaste la palabra: $palabraSecreta")
                break
            } else {
                println(" ¡Bien! Sigue así.")
            }
        } else {
            intentosRestantes--
            println(" La letra es incorrecta cach@n, te quedan $intentosRestantes intentos.")
        }
    }

    if (intentosRestantes == 0) {
        println(" Has perdido, tu no sirves, la palabra secreta era: $palabraSecreta")
    }
}

fun main() {
    jugarAhorcado()
}