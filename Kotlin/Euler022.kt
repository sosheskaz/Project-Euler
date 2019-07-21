package Euler022

import java.io.File
import java.util.Collections

fun main() {
    var names = loadFile("input/names.txt")
    Collections.sort(names)
    val s = names.asSequence().mapIndexed { idx, n -> scoreName(n) * (idx + 1) }.sum()
    println(s)
}

fun loadFile(path: String): List<String> {
    return File(path).readText().split(',').map { l -> l.replace("\\W".toRegex(), "") }
}

fun scoreName(name: String): Int {
    return name.toLowerCase().map { c -> scoreLetter(c) }.sum()
}

fun scoreLetter(c: Char): Int {
    return c - 'a' + 1
}
