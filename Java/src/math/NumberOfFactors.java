package math;

public class NumberOfFactors {
	
	public static int run(int num){
		
		if(num < 1){
			return -1; //invalid
		}
		if(num <= 2){ //if num = either 1 or 2
			return num;
		}
		
		int x = 2;
		int count = 2; //identity factors
		while(x <= num / 2){
			if(num % x == 0){
				count++;
			}
			x++;
		}
		
		return count;
	}
}
