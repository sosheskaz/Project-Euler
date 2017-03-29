import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.StringTokenizer;




public class n022 {
	public static void main(String[] args){
		try {
			Scanner fileScan = new Scanner(new File("/Users/ericmiller/Desktop/names.txt"));
			ArrayList names = new ArrayList();
			StringTokenizer st = new StringTokenizer(fileScan.nextLine(), "\",");
			
			long nameSum = 0;
			
			while(st.hasMoreTokens()){
				names.add(st.nextToken());
			}
			Collections.sort(names);
			
			for(int i = 0; i < names.size(); i++){
				int nameVal = getLetterSumValue(names.get(i).toString());
				nameVal *= i + 1;
				nameSum += nameVal;
			}
			System.out.printf("The sum of the values for all the names in the file is %d.", nameSum);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	private static int getLetterSumValue(String name){ //calculates the value for a single name
		int sum = 0;
		String n = name.toLowerCase();
		for(int i = 0; i < n.length(); i++){
			switch(n.charAt(i)){
			case 'z':
				sum++;
			case 'y':
				sum++;
			case 'x':
				sum++;
			case 'w':
				sum++;
			case 'v':
				sum++;
			case 'u':
				sum++;
			case 't':
				sum++;
			case 's':
				sum++;
			case 'r':
				sum++;
			case 'q':
				sum++;
			case 'p':
				sum++;
			case 'o':
				sum++;
			case 'n':
				sum++;
			case 'm':
				sum++;
			case 'l':
				sum++;
			case 'k':
				sum++;
			case 'j':
				sum++;
			case 'i':
				sum++;
			case 'h':
				sum++;
			case 'g':
				sum++;
			case 'f':
				sum++;
			case 'e':
				sum++;
			case 'd':
				sum++;
			case 'c':
				sum++;
			case 'b':
				sum++;
			case 'a':
				sum++;
			}
		}
		return sum;
	}
}
