import math.NumberOfFactors;


public class n012 {
	public static void main(String[] args){
		System.out.printf("Starting process...");
		int n = 1;
		int x = 1;
		int addition = 2;
		int iterations = 0;
		
		while(x < 500){
			n += addition;
			x = NumberOfFactors.run(n);
			addition++;
			
			iterations ++;
		}
		
		System.out.printf("%d", n);
		
		//System.out.printf("%d", NumberOfFactors.run(36));
	}
}
