package arrays;

/*
153. https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
*/
public class MinInSortedArray {

    public static int findMin(int[] nums) {
        int n= nums.length;
        if(n==1){
            return nums[0];
        }
        int i=0;
        int j=1;
        while(j<n && i<n && nums[j]>nums[i]){
            i++;
            j++;
        }
        if(j==n){
            return nums[0];
        }
        return nums[j];
    }
    public static void main(String args[]) {
        int[] nums = new int[] { 1,2,3,4};
        System.out.println("Result = " + findMin(nums));
    }
}
