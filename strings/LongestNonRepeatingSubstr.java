package strings;

import java.util.HashMap;
import java.util.Iterator;


// 3. https://leetcode.com/problems/longest-substring-without-repeating-characters/
public class LongestNonRepeatingSubstr {

    public static int lengthOfLongestSubstring(String s) {
        int n = s.length();
        if (n <= 1) {
            return n;
        }

        HashMap<Character, Integer> map = new HashMap<>();
        int maxLen = 1;
        int i = 0;
        int currlen = 0;
        int start = i;
        int indexOfMatchingChar;
        char currentChar;
        while (i < n) {
            currentChar = s.charAt(i);
            if (map.containsKey(currentChar) && map.get(currentChar)>=start) {
                if (currlen > maxLen) {
                    maxLen = currlen;
                }
                indexOfMatchingChar = map.get(currentChar);
                start = indexOfMatchingChar + 1;
                map.put(currentChar, i);
                currlen = i - start + 1;
            } else {
                map.put(currentChar, i);
                currlen += 1;
            }
            i += 1;
        }
        return currlen>maxLen ? currlen : maxLen;
    }

    public static void main(String args[]) {
        String name = "pwwkew";
        System.out.println("result = " + lengthOfLongestSubstring(name));
    }
}
