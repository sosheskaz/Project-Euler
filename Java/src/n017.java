
public class n017 {
	static final int ONE = 3;
	static final int TWO = 3;
	static final int THREE = 5;
	static final int FOUR = 4;
	static final int FIVE = 4;
	static final int SIX = 3;
	static final int SEVEN = 5;
	static final int EIGHT = 5;
	static final int NINE = 4;
	static final int TEN = 3;
	static final int ELEVEN = 6;
	static final int TWELVE = 6;
	static final int THIRTEEN = 8;
	static final int FOURTEEN = 8;
	static final int FIFTEEN = 7;
	static final int SIXTEEN = 7;
	static final int SEVENTEEN = 9;
	static final int EIGHTEEN = 8;
	static final int NINETEEN = 8;
	static final int TWENTY = 6;
	static final int THIRTY = 6;
	static final int FORTY = 5;
	static final int FIFTY = 5;
	static final int SIXTY = 5;
	static final int SEVENTY = 7;
	static final int EIGHTY = 6;
	static final int NINETY = 6;
	static final int HUNDRED = 7;
	

	public static void main(String[] args){
		int total = 11; //One Thousand
		for(int i = 1; i < 1000; i++){
			if(i >= 100){
				total += HUNDRED;
				switch( (int) (i / 100) ) {
				case 1:
					total += ONE;
					break;
				case 2:
					total += TWO;
					break;
				case 3:
					total += THREE;
					break;
				case 4:
					total += FOUR;
					break;
				case 5:
					total += FIVE;
					break;
				case 6:
					total += SIX;
					break;
				case 7:
					total += SEVEN;
					break;
				case 8:
					total += EIGHT;
					break;
				case 9:
					total += NINE;
				}

			}
			if(i % 100 != 0){
				if(i > 100){
					total += 3; //AND
				}
				switch(i % 100) {
				case 1:
					total += ONE;
					break;
				case 2:
					total += TWO;
					break;
				case 3:
					total += THREE;
					break;
				case 4:
					total += FOUR;
					break;
				case 5:
					total += FIVE;
					break;
				case 6:
					total += SIX;
					break;
				case 7:
					total += SEVEN;
					break;
				case 8:
					total += EIGHT;
					break;
				case 9:
					total += NINE;
					break;
				case 10:
					total += TEN;
					break;
				case 11:
					total += ELEVEN;
					break;
				case 12:
					total += TWELVE;
					break;
				case 13:
					total += THIRTEEN;
					break;
				case 14:
					total += FOURTEEN;
					break;
				case 15:
					total += FIFTEEN;
					break;
				case 16:
					total += SIXTEEN;
					break;
				case 17:
					total += SEVENTEEN;
					break;
				case 18:
					total += EIGHTEEN;
					break;
				case 19:
					total += NINETEEN;
					break;
				default:
					switch( (int) ((i % 100) / 10)) {
					case 2:
						total += TWENTY;
						break;
					case 3:
						total += THIRTY;
						break;
					case 4:
						total += FORTY;
						break;
					case 5:
						total += FIFTY;
						break;
					case 6:
						total += SIXTY;
						break;
					case 7:
						total += SEVENTY;
						break;
					case 8:
						total += EIGHTY;
						break;
					case 9:
						total += NINETY;
						break;
					}
					switch (i % 10) {
					case 1:
						total += ONE;
						break;
					case 2:
						total += TWO;
						break;
					case 3:
						total += THREE;
						break;
					case 4:
						total += FOUR;
						break;
					case 5:
						total += FIVE;
						break;
					case 6:
						total += SIX;
						break;
					case 7:
						total += SEVEN;
						break;
					case 8:
						total += EIGHT;
						break;
					case 9:
						total += NINE;
					}
				}
			}
		}
		System.out.printf("Total number of letters: %d", total);
	}
}
