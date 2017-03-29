import java.util.ArrayList;



public class n023 {
	public static void main(String[] args){
		boolean[] abundantNumbers = abundantNumbersGenerator();
		
		ArrayList<Integer> nonSums = nonSumsOfAbundants(abundantNumbers);
		
		int sum = 0;
		for(int i = 0; i < nonSums.size(); i++){
			sum += nonSums.get(i);
		}
		
		System.out.println(sum);
	}
	
	static ArrayList<Integer> nonSumsOfAbundants(boolean[] abundantNumbers){
		boolean[] abundantSums = new boolean[abundantNumbers.length];
		
		for(int a = 1; a < abundantNumbers.length; a++){
			if(abundantNumbers[a]){
				for(int b = 1; b < abundantNumbers.length; b++){
					if(abundantNumbers[b]){
						if(a+b < abundantNumbers.length){
							abundantSums[a+b] = true;
						}
					}
				}
				
			}
		}
		
		ArrayList<Integer> antiSums = new ArrayList<Integer>();
		
		for(int i = 1; i < abundantSums.length; i++){
			if(!abundantSums[i]){
				antiSums.add(i);
			}
		}
		
		return antiSums;
	}
	
	static boolean[] abundantNumbersGenerator(){
		int sum;
		boolean[] numbers = new boolean[28123];
		for(int i = 1; i <= 28122; i++){
			sum = 0;
			for(int i2 = 1; i2 <= i/2; i2++){
				if(i % i2 == 0){
					sum += i2;
				}
			}
			if(sum > i){
				
				numbers[i] = true;
				
			}
		}
		
		return numbers;
	}
	
}