package it_a2_harsh;
import java.util.Scanner;

public class IT_A2_Harsh_Array1D {
    
    public static void main(String[] args) {
        
        Scanner sin = new Scanner(System.in);
        
        int arr[] = new int[5];
        
        System.out.println("Scanning Data for Array:");
        for(int i = 0; i<5; i++)
        {
            System.out.println("Enter Element:");
            arr[i] = sin.nextInt();
        }
        
        System.out.println("Scanned Array:");

        
        for(int j : arr)
        {
            System.out.println(j);
        }
        
        
    }
    
}
