import java.util.HashMap;


public class n032 {
	public static void main(String[] args) {
		long total = 0;
		
		HashMap<Integer, Boolean> map = new HashMap<Integer, Boolean>();
		
		for(int a = 1; a < 20000; a++) {
			for(int b = 1; b < 20000; b++) {
				int product = b*a;
				if(product > 1000000000) {
					break;
				}
				String strRep = "" + a + b + product;
				boolean fail = false;
				
				if(strRep.length() != 9) {
					fail = true;
				}
				
				for(char c = '1'; c <= '9' && !fail; c++) {
					if(!strRep.contains("" + c)){
						fail = true;
					}
				}
				
				if(!fail) {
					if(!map.containsKey(product)) {
						total += (long) product;
						map.put(product, true);
						System.out.println("A: " + a + ", B: " + b + ", C: " + product);
					} else {
						System.out.println("A: " + a + ", B: " + b + ", C: " + product + ", DOUBLE");
					}
				}
			}
		}
		
		System.out.println("Total: " + total);
	}
}
