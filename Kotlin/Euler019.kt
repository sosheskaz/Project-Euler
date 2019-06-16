package Euler019

import java.util.Calendar

fun main() {
  val calendar = Calendar.getInstance()
  var sundays = 0

  for (year in 1901..2000) {
    for (month in Calendar.JANUARY..Calendar.DECEMBER) {
      calendar.set(year, month, 1)
      if (calendar.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) sundays++
    }
  }

  println(sundays)
}
