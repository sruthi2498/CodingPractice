package arrays;

// 53. https://leetcode.com/problems/maximum-subarray/

public class MaximumSubarray {

    public static int maxSubArray(int[] nums) {
        int max_so_far = -100001;
        int max_ending_here = 0;
        for(int i=0;i<nums.length;i++){
            max_ending_here += nums[i];
            if(max_ending_here >= max_so_far){
                max_so_far = max_ending_here;
            }
            if(max_ending_here<0){
                max_ending_here = 0;
            }
        }
        return max_so_far;
    }

    public static void main(String args[]) {
        int[] nums = new int[] { -2,1,-3,4,-1,2,1,-5,4 };
        System.out.println("Result = " + maxSubArray(nums));
    }
}
