import java.util.List;
import java.util.ArrayList;

class Euler003 {
  public static void main(String[] args) {
    ArrayList<Long> factors = primeFactors(600851475143L);
    System.out.println(factors.get(factors.size()-1));
  }

  private static ArrayList<Long> primeFactors(Long ofNumber) {
    ArrayList<Long> factors = new ArrayList<>();

    while (ofNumber % 2L == 0L) {
      ofNumber /= 2L;
      factors.add(2L);
    }

    for (Long i = 3L; i <= ofNumber; i += 2L) {
      if (ofNumber == 1L) {
        break;
      }

      while (ofNumber % i == 0) {
        ofNumber /= i;
        factors.add(i);
      }
    }

    return factors;
  }
}
