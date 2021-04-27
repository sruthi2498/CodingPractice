package arrays;

import java.util.*;

/*
https://leetcode.com/problems/contains-duplicate/
*/
public class ContainsDuplicate {

    public static boolean containsDuplicate(int[] nums) {

        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (set.contains(num)) {
                return true;
            }
            set.add(num);
        }

        return false;
    }

    public static void main(String args[]) {
        int[] nums = new int[] { -1, 0, 1, 2, -1, -4 };
        System.out.println("Result = " + containsDuplicate(nums));
    }
}
