package arrays;

import java.util.*;

/*
https://leetcode.com/problems/check-if-n-and-its-double-exist/
*/
public class CheckIfDoubleExists {

    public static boolean checkIfExist(int[] arr) {
        if(arr.length<=1){
            return false;
        }
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<arr.length;i++){
            if(map.containsKey(arr[i]*2) && map.get(arr[i]*2)!=i){
                return true;
            }
            else if(arr[i]%2 == 0 && map.containsKey(arr[i]/2) && map.get(arr[i]/2)!=i){
                return true;
            }
            map.put(arr[i],i);
        }
       
        return false;
        
    }

    public static void main(String args[]) {
        int[] nums = new int[] { 3,1,2};
        System.out.println("Result = " + checkIfExist(nums));
    }
}
