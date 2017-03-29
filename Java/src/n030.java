import java.math.BigDecimal;


public class n030 {
	public static void main(String[] args) {
		BigDecimal one = new BigDecimal(1);
		BigDecimal output;
		BigDecimal divisor;
		
		int biggest = 0;
		int d = 1;
		
		for(int i = 3; i < 1000; i++) {
			int tester = i;
			while(tester % 5 == 0) {
				tester /= 5;
			}
			while(tester %2 == 0) {
				tester /= 2;
			}
			
			if(tester != 1) {
				divisor = new BigDecimal(i);
				output = one.divide(divisor, 2000, BigDecimal.ROUND_UP);
				String analyzer = output.toPlainString();
				String checker = analyzer.substring(500, 900);
				int endIndex = analyzer.indexOf(checker, 501);
				int length = endIndex - 500;
				if(length > biggest) {
					biggest = length;
					d = i;
					System.out.println("D: " + d + ", Length: " + length);
				}
			}
		}
		
		System.out.println(d);
		System.out.println(biggest);
	}
}
