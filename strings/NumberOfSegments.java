package strings;

import java.util.Arrays;

// 434. https://leetcode.com/problems/number-of-segments-in-a-string/
public class NumberOfSegments {
    public static int countSegments(String s) {
        int n = s.length();
        if(n==0){
            return 0;
        }
        if(n==1){
            if(s.equals(" ")){
                return 0;
            }
            return 1;
        }
        int i = 0;
        
        while(i<n && s.charAt(i)==' '){
            i+=1;
        }
        if(i==n){
            return 0;
        }
        int count = 1;
        while(i<n){
            if(s.charAt(i)==' '){
                while(i<n && s.charAt(i)==' '){
                    i+=1;
                }
                if(i!=n){
                    count+=1;
                }
                
            }else{
                i+=1;
            }
        
        }
        return count;
    }
    public static void main(String args[]) {
        String name = "    ";
        System.out.println("result = "+countSegments(name));
    }
}
