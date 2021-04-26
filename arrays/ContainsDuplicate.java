package arrays;

import java.util.*;
/*
https://leetcode.com/problems/contains-duplicate/
*/
public class ContainsDuplicate {

    public static boolean containsDuplicate(int[] nums) {
        
        int n = nums.length;

        Set<Integer> set = new LinkedHashSet<>();
        for(int i=0;i<n;i++){
            if(set.contains(nums[i])){
                return true;
            }
            set.add(nums[i]);
        }



        return false;
    }
    public static void main(String args[]) {
        int[] nums = new int[] { -1,0,1,2,-1,-4};
        System.out.println("Result = " + containsDuplicate(nums));
    }
}
