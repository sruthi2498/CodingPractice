package arrays;

import java.util.HashSet;
import java.util.Hashtable;

public class TwoSum {

    public static int[] twoSum(int[] nums, int target) {
        int[] result = new int[]{-1,-1};
        Hashtable<Integer,Integer> differenceMap = new Hashtable<>();
        int diff,num;
        for(int i=0;i<nums.length;i++){
            num = nums[i];
            diff = target - num;
            if(differenceMap.get(diff)!=null){
                result[0] = differenceMap.get(diff);
                result[1] = i;
                return result;
            }
            differenceMap.put(num,i);
           // System.out.println("map : "+differenceMap);
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
