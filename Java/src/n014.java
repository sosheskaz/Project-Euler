public class n014 {
	
	static int[] checked = new int[10000000];
	static int greatest = 1;
	static int answer = 2;
	
	public static void main(String[] args){
		long start = System.nanoTime();
		checked[2] = 1;
		int x = 3;
		int y = 0;
		while(x <= 1000000){
			y = (int) calculateSteps(x);
			if(y > greatest){
				greatest = y;
				answer = x;
			}
			x++;
		}
		System.out.printf("The longest Collatz sequence comes from %d, at %d\n", answer, greatest);
		System.out.println(System.nanoTime()-start);
	}
	
	static long calculateSteps(long number){
		if(number >= 10000000){
			if(number % 2 == 0){
				return calculateSteps(number / 2) + 1;
			}
			return calculateSteps(number * 3 + 1) + 1;
		}
		if(checked[(int) number] != 0){
			return checked[(int) number] + 1;
		}
		if(number % 2 == 0){
			checked[(int) number] = (int) (calculateSteps(number / 2) + 1);
			return checked[(int) number];
		}
		checked[(int) number] = (int) (calculateSteps(number * 3 + 1) + 1);
		return checked[(int) number];
	}
	
}
