package arrays;

import java.util.HashSet;
import java.util.Hashtable;

// 1. https://leetcode.com/problems/two-sum/submissions/

public class TwoSum {

    public static int[] twoSum(int[] nums, int target) {
        int[] result = new int[]{-1,-1};
        Hashtable<Integer,Integer> differenceMap = new Hashtable<>();
        
        for(int i=0;i<nums.length;i++){
            if(differenceMap.get(target - nums[i])!=null){
                result[0] = differenceMap.get(target - nums[i]);
                result[1] = i;
                return result;
            }
            differenceMap.put(nums[i],i);
        }

        return result;
    }
    public static void main(String args[]) 
    {
        int[] nums = new int[]{2,7,11,15};
        int target = 9;
        int[] result = twoSum(nums,target);
        System.out.println("Result = "+ result[0]+","+result[1] );
    }
}
