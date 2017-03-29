import java.math.BigInteger;


public class n020 {
	public static void main(String[] args){
		BigInteger big = new BigInteger("100");
		
		for(int i = 99; i > 1; i--){
			big = big.multiply(new BigInteger(""+i));
		}
		int sum = 0;
		String s = big.toString();
		for(int i = 0; i < s.length(); i++){
			sum += (Integer.parseInt(""+ s.charAt(i)));
		}
		
		System.out.println(sum);
	}
}
