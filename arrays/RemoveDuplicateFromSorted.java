package arrays;

import java.util.*;

/*
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
*/
public class RemoveDuplicateFromSorted {

    public static int removeDuplicates(int[] nums) {
        int i = 0;
        int n = nums.length;
        if(n<=1){
            return n;
        }
        int j = i+1;
        //System.out.println(Arrays.toString(nums));
        while(i<n && j<n){
            while(j<n && nums[j]==nums[i]){
                j+=1;
            }
            if(j>=n){
                return i+1;
            }
            if(i+1<n && j>i+1){
                nums[i+1]= nums[j];
            }
            i+=1;
            j+=1;
            //System.out.println(Arrays.toString(nums));

        }
        return i+1;
    }

    public static void main(String args[]) {
        int[] nums = new int[] { 1,1};
        System.out.println("Result = " + removeDuplicates(nums));
    }
}
