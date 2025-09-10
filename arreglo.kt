import kotlin.random.Random

fun main() {
    // (Opcional) Para reproducibilidad: val rnd = Random(42)
    val rnd = Random.Default

    // IntArray de tamaño 10 con valores aleatorios 1..100
    val arreglo = IntArray(10) { rnd.nextInt(1, 101) } // upper bound es exclusivo -> 101

    println("Arreglo (IntArray) de 10 enteros aleatorios:")
    println(arreglo.joinToString(prefix = "[", postfix = "]", separator = ", "))

    // Mostrar con índice
    for (i in arreglo.indices) {
        println("Índice $i: ${arreglo[i]}")
    }
}
