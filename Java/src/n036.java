
public class n036 {
	public static void main(String[] args) {
		int sum = 0;
		for(int i = 1; i < 1000000; i++) {
			if(isPalindrome("" + i) && isPalindrome(Integer.toBinaryString(i))) {
				sum += i;
			}
		}
		System.out.println(sum);
	}
	
	private static boolean isPalindrome(String s) {
		char[] chars = s.toCharArray();
		for(int i = 0; i < chars.length / 2; i++) {
			if(chars[i] != chars[chars.length - 1 - i]) {
				return false;
			}
		}
		return true;
	}
}
