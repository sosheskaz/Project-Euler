import java.util.LinkedList;
import java.util.TreeMap;


public class n035 {
	public static void main(String[] args) {
		LinkedList<Integer> primes = new LinkedList<Integer>();
		TreeMap<Integer, Object> shiftables = new TreeMap<Integer, Object>();
		primes.add(2);
		for(int i = 3; i < 1000000; i++) {
			isPrime(primes, i);
		}
		TreeMap<Integer, Object> primeTree = new TreeMap<Integer, Object>();
		for(int prime : primes) {
			primeTree.put(prime, null);
		}
		
		for(int prime : primes) {
			int[] shifts = getAllShifts(prime);
			boolean success = true;
			for(int i = 0; i < shifts.length; i++) {
				if(!primeTree.containsKey(shifts[i])) {
					success = false;
					break;
				}
			}
			if(success) {
				for(int i = 0; i < shifts.length; i++) {
					if(!shiftables.containsKey(shifts[i])){
						shiftables.put(shifts[i], null);
					} else {
						break;
					}
				}
			}
		}
		
		System.out.println(shiftables.size());
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
	
	private static int[] getAllShifts(int n) {
		int length = (int) Math.log10(n) + 1;
		int[] numbers = new int[length];
		for(int i = 0; i < length; i++) {
			numbers[length - 1 - i] = n % 10;
			n /= 10;
		}
		
		int[] output = new int[length];
		for(int i = 0; i < length; i++) {
			int product = 0;
			for(int j = i; j < length + i; j++) {
				product += numbers[j % length];
				product *= 10;
			}
			product /= 10;
			output[i] = product;
		}
		
		return output;
	}
}
