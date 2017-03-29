/**
 * 
 */
package euler;

import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * 
 * 
 * Author: Eric Miller
 * Date: Sep 7, 2014
 */
public class euler026 {
    public static void main(String[] args)
    {
	int longest = 0;
	String num = "";
	for(double d = 2; d <= 1000; d++)
	{
	    MathContext mc = new MathContext(20000, RoundingMode.DOWN);
	    BigDecimal dec = new BigDecimal(1).divide(new BigDecimal(d), mc);
	    String s = "" + dec.toString(); 
	    s = s.substring(2);
	    int comp = getRepeatLength(s);
	    if(comp >= longest)
	    {
		longest = comp;
		num += "d: " + d + " " + comp + ", ";
	    }
	    
	    System.out.println("d: " + d + ", S: " + s + (comp == longest ? " pat: " + comp : ""));
	}
	
	System.out.println(num);
    }
    
    private static int getRepeatLength(String n)
    {
	Pattern p = Pattern.compile("(([0-9]{1,})\\1)");
	Matcher m = p.matcher(n);
	if(!m.find())
	{
	    return n.length();
	}
	else
	{
	    System.out.println("Pattern: " + m.group(1));
	    return getRepeatLength(m.group(1));
	}
    }
}
