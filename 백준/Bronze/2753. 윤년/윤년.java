import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        boolean isYoon = false;
        if(n % 100 != 0 ){
            if(n % 4 == 0){
                isYoon = true;
            }
        } else {
            if(n % 400 == 0){
                isYoon = true;
            }
        }
        
        if (isYoon) System.out.println(1);
        else System.out.println(0);
        
    }
}