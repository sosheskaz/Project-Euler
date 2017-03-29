
public class n024 { // lexicographic permutations
	public static void main(String[] args){
		int[] out = {1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000};
		
		int num = 1000000;
		
		int x = 0;
		
		for(int i = 0; i < 9; i++){
			x = num / getPermutation(10-i-1);
			num = num % getPermutation(10-i-1);
			
			boolean check = false;
			boolean[] whitelist = new boolean[10];
			/*while(!check){
				int[] checks = {0, 0};
				for(int q = 0; q < 10; q++){
					if(out[q] <= x && whitelist[q] == false){
						x++;
						whitelist[q] = true;
					}
				}
				checks[0] = x;
				for(int q = 0; q < 10; q++){
					if(out[q] <= x && whitelist[q] == false){
						x++;
						whitelist[q] = true;
					}
				}
				checks[1] = x;
				if(checks[0] == checks[1]){
					check = true;
					System.out.println("check, "+x);
				}
				System.out.printf("%d\t%d\t%d\n", x, checks[0], checks[1]);
			}*/
			
			out[i] = x;
		}
		for(int i = 0; i < 10; i++){
			
			System.out.println(out[i]);
		}
	}
	
	public static int getPermutation(int x){
		for(int i = x; i > 1; i--){
			x*= i;
		}
		return x;
	}
}
