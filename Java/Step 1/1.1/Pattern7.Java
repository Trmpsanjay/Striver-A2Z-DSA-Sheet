/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int row = sc.nextInt();
		for(int i=0;i<row;i++){
		    // printing space 
		    for(int space=0;space<=row-i-1;space++){
		        System.out.print(" ");
		    }
		    //printing star 
		    for(int j=0;j<2*i+1;j++){
		        System.out.print("*");
		    }
		    System.out.println();
		}
	}
}
