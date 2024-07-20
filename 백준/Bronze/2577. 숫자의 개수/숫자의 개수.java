import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        String abc = String.valueOf(a*b*c);
        for (int i=0; i<=9; i++){
            countDigit(abc,i);
        }
    }

    public static void countDigit(String str, int digit) {
        int count = 0;
        Integer digitInteger = digit;
        for (int i = 0; i < str.length(); i++) {
            String charDigit = str.charAt(i) + "";
            if (digitInteger.toString().equals(charDigit)) {
                count += 1;
            }
        }
        System.out.println(count);
            
        
    }
}