
public class n015 {
	public static void main(String[] args){
		long[][] triangle = new long[41][];
		
		int x = 1;
		
		for(int i = 0; i <= 40; i++){
			triangle[i] = new long[x];
			triangle[i][0] = 1;
			triangle[i][triangle[i].length - 1] = 1;
			for(int z = 1; z < triangle[i].length - 1; z++){
				triangle[i][z] = triangle[i-1][z-1] + triangle[i-1][z];
			}
			x++;
		}
		
		System.out.println(triangle[40][20]);
	}
}
