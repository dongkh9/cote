import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int nowNum = sc.nextInt();
        if (nowNum != 1 && nowNum != 8){
            System.out.println("mixed");
        } else if (nowNum == 1){
            boolean isAscending = true;
            int i = 0;
            while(isAscending && i<7){
                int nextNum = sc.nextInt();
                isAscending = isItAscending(nowNum,nextNum);
                if (!isAscending) break;
                i++;
                nowNum = nextNum;
            }
            if (isAscending) System.out.println("ascending");
            else System.out.println("mixed");
        } else {
            boolean isDescending = true;
            int i = 0;
            while(isDescending && i<7){
                int nextNum = sc.nextInt();
                isDescending = isItDescending(nowNum,nextNum);
                if (!isDescending) break;
                i++;
                nowNum = nextNum;
            }
            if (isDescending) System.out.println("descending");
            else System.out.println("mixed");
        }
    }
    
    public static boolean isItAscending(int fstNum, int sndNum){
        boolean isAscending = false;
        if (fstNum + 1 == sndNum){
            isAscending = true;
        }
        return isAscending;
    }
    public static boolean isItDescending(int fstNum, int sndNum){
        boolean isDescending = false;
        if (fstNum -1 == sndNum){
            isDescending = true;
        }
        return isDescending;
    }
}