package strings;

// 1758 https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

public class MinChangesBinary {

    public static int minOperations(String s) {
        int n = s.length();
        if(n==1){
            return 0;
        }
        char currentChar1 = '1';
        int count1 = 0;

        char currentChar2 = '0';
        int count2 = 0;
        for(int i=0;i<n;i++){
            if(s.charAt(i)!=currentChar1){
                count1+=1;
            }else{
                count2+=1;
            }
            currentChar1 = (currentChar1 == '1') ? '0' : '1';
            currentChar2 = (currentChar2 == '1') ? '0' : '1';
        }

        
        return Math.min(count1,count2);
        
    }
    public static void main(String args[]) {
        String num = "1111";
        System.out.println("Result = " + minOperations(num));
    }
}
