package arrays;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

// 169. https://leetcode.com/problems/majority-element/
public class MajorityElementOne {
    public static int majorityElement(int[] nums) {
        int n = nums.length;
        if(n==1){
            return nums[0];
        }
        int maj_elem = nums[0];
        int maj_count = 1;
        int i=1;
        while(i<n){
            if(nums[i]==maj_elem){
                maj_count++;
            }else{
                if(maj_count == 1){
                    maj_elem = nums[i];
                }else{
                    maj_count--;
                }
            }
            i+=1;
        }
        return maj_elem;
        
    }

    public static void main(String args[]) {
        int[] nums = new int[]{3,2,3};
        System.out.println("result = "+majorityElement(nums));
    }
}
