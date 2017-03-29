package euler;

import java.util.LinkedList;

public class euler024 {
    private static final int[] OPTIONS = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    private static boolean[] visited = {false, false, false, false, false, false, false, false, false, false};
    private static LinkedList<Integer> currentPath = new LinkedList<>();
    
    
    private static int numberDone = 0;
    
    public static void main(String[] args) {
	for(int i = 0; i < 10; i++) {
	    visited[i] = true;
	    recurse(i);
	    visited[i] = false;
	}
    }
    
    private static void recurse(int num) {
	visited[num] = true;
	currentPath.add(num);
	if(currentPath.size() == 10) {
	    numberDone++;
	    if(numberDone == 1000000) {
		for(int val : currentPath) {
		    System.out.print(val);
		}
	    }
	} else {
	    for(int i = 0; i < 10; i++) {
		if(!visited[i]) {
		    recurse(i);
		}
	    }
	}
	visited[num] = false;
	currentPath.remove(currentPath.size() - 1);
    }
    
}
