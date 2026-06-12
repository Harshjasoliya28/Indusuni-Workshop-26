package it_a2_harsh;
import java.util.Scanner;

public class IT_A2_Harsh_Circle {
    
    public static void main(String[] args) {
        
        Scanner sin = new Scanner(System.in);
        
        System.out.println("Enter The Radius of Circle: ");
        int rad = sin.nextInt();
        float area = 3.14f*rad*rad;
        System.out.println("The Area of Circle having radius "+rad+" cm, is "+area);
        
    }
    
}
