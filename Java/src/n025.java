import java.math.BigInteger;


public class n025 {
	
	public static void main(String[] args){
		BigInteger[] x = new BigInteger[3];
		x[0] = new BigInteger("1"); x[1] = new BigInteger("1"); x[2] = new BigInteger("2");
		int n = 3;
		
		BigInteger C = new BigInteger("10");
		C = C.pow(999);
		
		while(x[2].compareTo(C) == -1){
			x[0] = x[1];
			x[1] = x[2];
			x[2] = getNextFibonacci(x);
			
			n++;
		}
		
		System.out.println(x[2]);
		System.out.println(n);
	}
	
	static BigInteger getNextFibonacci(BigInteger[] x){
		return x[1].add(x[0]);
	}
}
