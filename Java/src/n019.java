import java.util.Calendar;


public class n019 {
	public static void main(String[] args){
		Calendar cal = Calendar.getInstance();
		cal.set(1901, 1, 1);
		Calendar compare = Calendar.getInstance(); compare.set(2000, 12, 31);
		int count = 0;
		
		while(cal.get(cal.DAY_OF_WEEK) != cal.SUNDAY){
			cal.add(cal.DAY_OF_MONTH, 1);
		}
		while(cal.before(compare) ){
			if(cal.get(cal.DAY_OF_MONTH) == 1){
				count++;
			}
			cal.add(cal.DAY_OF_MONTH, 7);
		}
		System.out.println(count);
	}
}
