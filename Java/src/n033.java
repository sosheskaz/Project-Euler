
public class n033 {
	public static void main(String[] args) {
		int num = 1;
		int den = 1;
		
		for(int i = 11; i < 99; i++) {
			for(int j = i + 1; j < 99; j++) {
				double fraction = ((double) i) / ((double) j);
				if(i % 10 == j / 10) {
					double subFraction = ((double) (i / 10)) / ((double) (j % 10));
					if(fraction == subFraction) {
						num *= i;
						den *= j;
					}
				}
			}
		}
		//This HAPPENS to reduce it nicely.
		System.out.println(num / num + "/" + den / num);
	}
}
