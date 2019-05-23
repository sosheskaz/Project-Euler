#!/usr/bin/env groovy
import java.util.Calendar
import java.util.Date

class Euler019 {
  public static void main(String[] args) {
    Calendar calendar = Calendar.getInstance();
    int sundays = 0

    // Java Calendar counts from 1900.
    for (int year = 1; year <= 100; year++) {
      for (int month = 1; month <= 12; month++) {
        Date d = new Date(year, month, 1)
        calendar.setTime(d)
        if (calendar.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) {
          sundays++
        }
      }
    }

    println sundays
  }
}
