import java.util.Scanner;
import java.util.HashSet;
public class Main{
    public static void main(String[] args){
        HashSet<Integer> set = new HashSet<>();
        Scanner sc = new Scanner(System.in);
        for (int i=0; i<10; i++){
            int nowNum = sc.nextInt();
            nowNum %= 42;
            set.add(nowNum);
        }
        System.out.println(set.size());
    }
}