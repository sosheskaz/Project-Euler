import java.math.BigInteger;


public class n016 {
	static long all = (long) Math.pow(2, 50);
	public static void main(String[] args){
		BigInteger biggiebigs = new BigInteger("2");
		biggiebigs = biggiebigs.pow(1000);
		String s = biggiebigs.toString();
		all = 0;
		for(int i = 0; i < s.length(); i++){
			all += Long.parseLong(s.substring(i, i+1));
		}
		
		System.out.println(all);
	}
	
}
