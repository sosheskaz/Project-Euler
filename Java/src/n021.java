import java.util.LinkedList;
import java.util.List;


public class n021 {
	public static void main(String[] args){
		
		List amicables = new LinkedList();
		
		for(int i = 2; i <= 10000; i++){
			
			int crosscheck = getDN(i);
			if(getDN(crosscheck) == i && getDN(i) != i){
				amicables.add(i);
			}
			
			
			
		}
		int sum = 0;
		for(int i = 0; i < amicables.size(); i++){
			sum += (Integer) amicables.get(i);
		}
		System.out.println(sum);
	}
	
	static int getDN(int number){
		int i = number;
		
		List divisors = new LinkedList();
		
		for(int x = 1; x < i; x++){
			if(i % x == 0){
				divisors.add(x);
			}
		}
		int sum = 0;
		
		for(int x = 0; x < divisors.size(); x++){
			sum += (Integer) divisors.get(x);
		}
		
		return sum;
	}
}
