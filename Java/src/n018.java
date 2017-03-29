import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;


public class n018 {
	public static void main(String[] args){
		System.out.print("Enter the number of rows: ");
		Scanner s = new Scanner(System.in);
		int rows = s.nextInt();
		
		System.out.println("Enter your numbers, in triangle format.");
		
		String numbers = s.nextLine();
		List integers = new LinkedList();
		StringTokenizer st = new StringTokenizer(s.nextLine());
		while(st.hasMoreTokens()){
			integers.add(Integer.parseInt(st.nextToken()));
		}
		
		int[][] triangle = new int[rows][];
		for(int i = 0; i < rows; i++){
			triangle[i] = new int[i + 1];
		}
		int pos = 0;
		for(int i = 0; i < rows; i++){ //inputs
			for(int x = 0; x < triangle[i].length; x++){
				triangle[i][x] = (Integer) integers.get(pos);
				pos++;
			}
		}
		System.out.printf("%d\t%d\t%d\t", triangle[0][0], triangle[1][0], triangle[1][1]);
		for(int i = 1; i < rows; i++){ //calculating subtriangle
			triangle[i][0] += triangle[i-1][0];
			triangle[i][triangle[i].length - 1] += triangle[i-1][triangle[i].length - 2];
			//above takes care of edges (which have only 1 parent)
			
			for(int x = 1; x < triangle[i - 1].length; x++){ //goes through row to calculate subtriangle
				if(triangle[i-1][x-1] > triangle[i-1][x]){
					triangle[i][x] += triangle[i-1][x-1];
				} else {
					triangle[i][x] += triangle[i-1][x];
				}
			}
		}
		int greatest = triangle[rows-1][0];
		for(int i = 1; i < rows; i++){
			if(triangle[rows - 1][i] > greatest){
				greatest = triangle[rows - 1][i];
			}
		}
		
		System.out.printf("\n\nThe greatest path amounts to %d.", greatest);
		
		
	}
	
	
}
