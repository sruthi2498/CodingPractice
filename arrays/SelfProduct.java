package arrays;

import java.util.Arrays;

/*
238. https://leetcode.com/problems/product-of-array-except-self/
*/

public class SelfProduct {

    public static int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        
        boolean containsZero = false;
        boolean containsMoreThanOneZero = false;
        for (int i = 0; i < n; i++) {
            if(nums[i] == 0 && containsZero ){
                containsMoreThanOneZero = true;
            }
            if (nums[i] == 0) {
                containsZero = true;
            }
        }

        int nonZeroProduct = 1;
        boolean nonZeroProductFound = false;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nonZeroProduct *= nums[i];
                nonZeroProductFound = true;
            }

        }

        boolean allZeroes = !nonZeroProductFound;

        if(allZeroes || containsMoreThanOneZero){
            for (int i = 0; i < n; i++) {
                result[i] = 0;
            } 
        }
        else if (containsZero) {
            for (int i = 0; i < n; i++) {
                if (nums[i] == 0) {
                    result[i] = nonZeroProduct;
                } else {
                    result[i] = 0;
                }
            }
           
        } 
        else {

            for (int i = 0; i < n; i++) {
                result[i] = nonZeroProduct / nums[i];

            }
        }

        return result;
    }

    public static void main(String args[]) // static method
    {
        // x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
        int[] nums = new int[] { 0,0,5,0};
        System.out.println("Result = " + Arrays.toString(productExceptSelf(nums)));
    }
}
