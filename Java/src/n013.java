import java.math.BigInteger;

import javax.swing.JOptionPane;


public class n013 {
	public static void main(String[] args){
		String str = JOptionPane.showInputDialog("Enter the number:");
		System.out.printf("Please wait while your sum is calculated...");
		
		str = removeChar(str, '\n');
		str = removeChar(str, ' ');
		
		BigInteger sum = new BigInteger("0");
		int max = str.length();
		int pos = 0;
		
		while(pos + 50 <= max){
			sum = sum.add(new BigInteger(str.substring(pos, pos + 50)));
			pos += 50;
		}
		
		System.out.printf("\n\nSum is %s", sum.toString());
	}
	
	public static String removeChar(String s, char c){
		while(s.contains(""+c)){
			s = s.substring(0, s.indexOf(c)) + s.substring(s.indexOf(c) + 1);
		}
		return s;
	}
}
