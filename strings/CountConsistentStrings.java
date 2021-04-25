package strings;

import java.sql.Array;
import java.util.Dictionary;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Map;

/*
1684. https://leetcode.com/problems/count-the-number-of-consistent-strings/
You are given a string allowed consisting of distinct characters and an array of strings words. 
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.*/

class Solution {


    public static int countConsistentStrings(String allowed, String[] words) {
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray(); 
        Hashtable<Character,Integer> alloweDictionary = new Hashtable<>();
        for(char letter : alphabet){
            alloweDictionary.put(letter, 0);
        }
        for(char letter: allowed.toCharArray()){
            alloweDictionary.put(letter,1);
        }
        int count = 0;
        for(String word : words){
            int i = 0;
            while(i<word.length() && alloweDictionary.get(word.charAt(i))==1){
                i+=1;
            }
            if(i==word.length()){
                count+=1;
            }
        }
        return count;
    }

    public static void main(String args[]) // static method
    {
        String allowed = "cade";
        String[] words = new String[]{"cc","acd","b","ba","bac","bad","ac","d"};
    
        System.out.println("Result = "+ countConsistentStrings(allowed,words));
    }
}
