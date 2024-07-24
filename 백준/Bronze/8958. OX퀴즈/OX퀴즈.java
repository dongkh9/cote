import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for(int i=0; i<n; i++){
            String line = sc.nextLine();
            int[] oList = makeO(line);
            int point = calPoint(oList);
            System.out.println(point);
        }
        
    }
    
    public static int[] makeO(String str){
        String[] remainO = str.split("X+");
        int[] numOfO = new int[remainO.length];
        for (int i=0; i<remainO.length; i++){
            numOfO[i] = remainO[i].length();
        }
        return numOfO;
    }
    public static int calPoint(int[] numOfO){
        int sum = 0;
        for(int O : numOfO){
            int sumToO = O*(O+1)/2;
            sum += sumToO;
        }
        return sum;
    }
}
