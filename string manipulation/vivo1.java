/*****************************************************
幸运数字“7” 
找出7的倍数或者含有7
*****************************************************/

import java.util.Scanner;

public class vivo1{
     public static void main(String []args){
        Scanner scanner = new Scanner(System.in);
        String s[] = scanner.nextLine().split(" ");
        int len = s.length;
        int res = 0;
        for (int i=0; i < len; i++){
            int flag = 0;
            int num = Integer.parseInt(s[i]);
            int stringlen = s[i].length();
            if (num%7==0) flag = 1;
            if (flag==0) {
                for (int j = 0; j < stringlen; j++) {
                    if (s[i].charAt(j) == '7') {
                        flag = 1;
                    }
                }                
            }
            if (flag==1) res++;
        }
        System.out.println(res);
     }
}
