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
        // primary loop
        for(int i=0;i<row;i++){
            //printing first half
            for(int j=0;j<=i;j++){
                 System.out.print("*");
            }
            System.out.println();
        }
         //printing second half
        for(int i=0;i<row;i++){
            //printing first half
            for(int j=0;j<row-i-1;j++)
                System.out.print("*");
            System.out.println();
        }
        
		    
	}
}
