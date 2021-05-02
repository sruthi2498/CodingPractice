package strings;

// 92. https://leetcode.com/problems/long-pressed-name/
public class LongPressedName {

    public static boolean isLongPressedName(String name, String typed) {
        int n = name.length();
        int m = typed.length();
        if(m<n){
            return false;
        }
        int i = 0;
        int j = 0;
        char currentChar;
        int currentCharCount, currentCharCountInTyped;
        while(i<n && j<m){
            currentChar = name.charAt(i);
            currentCharCount = 1;
            while(i+1 < n &&  name.charAt(i+1)==currentChar){
                i+=1;
                currentCharCount+=1;
            }
            currentCharCountInTyped = 0;
            while(j<m && typed.charAt(j)== currentChar){
                j+=1;
                currentCharCountInTyped+=1;
            }
            
            if(currentCharCountInTyped < currentCharCount){
                return false;
            }
            i+=1;
        } 
        if(j<m){
            return false;
        }
        if(i<n && j>=m){
            return false;
        }
        return true;
    }
    public static void main(String args[]) {
        String name = "pyp";
        String typed = "abc";
        System.out.println("result = "+isLongPressedName(name,typed));
    }
}
