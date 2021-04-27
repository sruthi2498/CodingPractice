package arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Hashtable;
import java.util.List;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.IntStream;
import java.util.LinkedHashSet;
import java.util.Enumeration;

/*
15. https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
*/
public class ThreeSum {


    public static List<List<Integer>> threeSum(int[] nums) {
       
        Set<List<Integer>> resultSet = new LinkedHashSet<>();
        List<Integer> triplet;
        int num,currSum, currSum2, k;
        for(int i=0;i<nums.length;i++){
            
            Hashtable<Integer,Integer> hashtable = new Hashtable<>();

            num = nums[i];
            currSum = -num;
            for(int j=i+1;j<nums.length;j++){
                currSum2 = currSum - nums[j];
                if(hashtable.get(currSum2) != null){
                    k = hashtable.get(currSum2);
                    if(k!= j && k!= i){
                        triplet = new ArrayList<>();
                        triplet.add(num);
                        triplet.add(currSum2);
                        triplet.add(nums[j]);
                        Collections.sort(triplet);
                        resultSet.add(triplet);
                    }
                }
                hashtable.put(nums[j], j);
            }
            
            
        }

        List<List<Integer>> result = new ArrayList<>();
        result.addAll(resultSet);
        return result;
    }

    public static void main(String args[]) {
        int[] nums = new int[] { -1,0,1,2,-1,-4};
        List<List<Integer>> result = threeSum(nums);
        System.out.println("Result = " + result.toString());
    }
}
