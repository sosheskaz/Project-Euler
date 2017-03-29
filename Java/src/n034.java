
public class n034 {
	public static void main(String[] args) {
		for(int i = 3; i < 100000; i++) {
			if(sumOfDigitFactorials(i) == i) {
				System.out.println(i);
			}
		}
	}
	
	private static int factorial(int n) {
		int product = 1;
		for(int i = 2; i <= n; i++) {
			product *= i;
		}
		return product;
	}
	
	private static int sumOfDigitFactorials(int n) {
		int sum = 0;
		while(n > 0) {
			sum += factorial(n % 10);
			n /= 10;
		}
		
		return sum;
	}
}
