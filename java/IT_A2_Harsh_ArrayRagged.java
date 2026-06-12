package it_a2_harsh ;
import java.util.Scanner;

public class IT_A2_Harsh_ArrayRagged {
    
    public static void main(String[] args) {
        
        Scanner sin = new Scanner(System.in);
        
        int rows = 2;
        int arr[][] = new int[rows][];
                arr[0] = new int[2];
                arr[1] = new int[3];
        
        System.out.println("Scanning Data for Array:");
        for(int i = 0; i<rows; i++)
        {
            for(int j = 0; j<arr[i].length; j++)
            {
                System.out.println("Enter Element for "+(i+1)+" Row and "+(j+1)+" Column:");
                arr[i][j] = sin.nextInt();
            }
        }
        
        System.out.println("Scanned Array:");

        for(int i = 0; i<rows; i++)
        {
            for(int j = 0; j<arr[i].length; j++)
            {
                System.out.println("Element for "+(i+1)+" Row and "+(j+1)+" Column:");
                System.out.println(arr[i][j]);
            }
        }
        
        
        
        
    }
    
}
