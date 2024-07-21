import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        for(int i=0; i<t; i++){
            int r = sc.nextInt();
            String s = sc.next();
            sc.nextLine();
            System.out.println(repString(s,r));
        }
    }
    
    public static String repString(String str,int rep){
        String result = "";
        for(int i=0; i<str.length(); i++){
            char characterAt = str.charAt(i);
            result += repChar(characterAt,rep); 
        }
        return result;
    }
    
    public static String repChar(char ch, int rep){
        String result = "";
        for(int i=0; i<rep; i++){
            result += ch;
        }
        return result;
    }
}