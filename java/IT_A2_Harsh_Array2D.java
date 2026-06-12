package it_a2_harsh ;
import java.util.Scanner;

public class IT_A2_Harsh_Array2D {
    
    public static void main(String[] args) {
        
        Scanner sin = new Scanner(System.in);
        
        int rows = 2;
        int cols = 2;
        int arr[][] = new int[rows][cols];
        
        System.out.println("Scanning Data for Array:");
        for(int i = 0; i<rows; i++)
        {
            for(int j = 0; j<cols; j++)
            {
                System.out.println("Enter Element for "+(i+1)+" Row and "+(j+1)+" Column:");
                arr[i][j] = sin.nextInt();
            }
        }
        
        System.out.println("Scanned Array:");

        for(int i = 0; i<rows; i++)
        {
            for(int j = 0; j<cols; j++)
            {
                System.out.println("Element for "+(i+1)+" Row and "+(j+1)+" Column:");
                System.out.println(arr[i][j]);
            }
        }
        
        
        
        
    }
    
}
