public class n031 {
	private static final int[] coins = new int[] {200, 100, 50, 20, 10, 5, 2, 1};
	
	public static void main(String[] args) {
		System.out.println(recurse(200, 0));
	}
	public static int recurse(int penceRemaining, int coinIndex){
		if(penceRemaining == 0) {
			return 1;
		}
		if(coins[coinIndex] == 1) {
			return 1;
		}
		int possibleCoins = penceRemaining / coins[coinIndex];
		int output = 0;
		for(int i = 0; i <= possibleCoins; i++){
			output += recurse(penceRemaining - i * coins[coinIndex], coinIndex + 1);
		}
		return output;
	}
}