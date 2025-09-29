import kotlin.random.Random

fun main() {
    // Arreglo de 10 enteros aleatorios (1..100)
    val arreglo = IntArray(10) { Random.nextInt(1, 100) }

    println("Arreglo creado: ${arreglo.joinToString(", ")}")

    // recorrido usando for clásico usando índices
    println("\nFor clásico:")
    for (i in arreglo.indices) {
        println("Índice $i: ${arreglo[i]}")
    }

    // recorrido usando for-each
    println("\nFor-each:")
    for (valor in arreglo) {
        println("Valor: $valor")
    }

    // modificación: si es impar lo cambiamos a 0, luego multiplicamos por índice
    for (i in arreglo.indices) {
        if (arreglo[i] % 2 != 0) {
            arreglo[i] = 0
        }
        arreglo[i] *= i
    }

    println("\nArreglo modificado: ${arreglo.joinToString(", ")}")

    // búsqueda lineal
    val resultado = busquedaLineal(arreglo, 50)
    println("Resultado búsqueda: $resultado")
}

// Función búsqueda lineal
fun busquedaLineal(arr: IntArray, valor: Int): Int {
    for (i in arr.indices) {
        if (arr[i] == valor) {
            return i
        }
    }
    return -1
}
