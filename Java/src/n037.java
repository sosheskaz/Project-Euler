import java.util.LinkedList;
import java.util.TreeMap;


public class n037 {
	static TreeMap<Integer, Object> primeTree = new TreeMap<Integer, Object>();
	
	public static void main(String[] args) {
		LinkedList<Integer> primes = new LinkedList<Integer>();
		primes.add(2);
		for(int i = 3; i < 1000000; i++) {
			isPrime(primes, i);
		}
		
		for(int prime : primes) {
			primeTree.put(prime, null);
		}
		System.out.println("Primes Calculated.");
		
		int count = 0;
		int sum = 0;
		int i = 10;
		while(count < 11) {
			if(isTruncatableRight(i) && isTruncatableLeft(i)) {
				sum += i;
				count++;
				System.out.println("Found: " + i);
			}
			i++;
		}
		System.out.println(sum);
	}
	
	private static boolean isTruncatableRight(int n) {
		if(n == 0) {
			return true;
		}
		if(primeTree.containsKey(n)) {
			int power = (int) Math.log10(n);
			int magnitude = (int) Math.pow(10, power);
			int coefficient = n / magnitude;
			int nextCheck = n - (coefficient * magnitude);
			return isTruncatableRight(nextCheck);
		} else {
			return false;
		}
	}
	
	private static boolean isTruncatableLeft(int n) {
		if(n == 0) {
			return true;
		}
		if(primeTree.containsKey(n)) {
			return isTruncatableLeft(n / 10);
		} else {
			return false;
		}
	}
	
	private static boolean isPrime(LinkedList<Integer> smallerPrimes, int n) {
		for(int prime : smallerPrimes) {
			if(n % prime == 0) {
				return false;
			}
		}
		smallerPrimes.add(n);
		return true;
	}
}
