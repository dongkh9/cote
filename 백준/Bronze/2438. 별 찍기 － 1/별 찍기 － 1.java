import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i=1; i<=n ; i++){
            placeStars(i);
            System.out.println();
        }
    }
    public static void placeStars(int num){
        for (int i=0 ; i<num ; i++ ) {
            System.out.print("*");
        }
    }
}