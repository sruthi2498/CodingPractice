package arrays;


// 896 https://leetcode.com/problems/monotonic-array/
public class MonotonicArray {

    public static boolean isMonotonic(int[] A) {
        int n = A.length;
        if(n<3){
            return true;
        }
        int j=1;
        while(j<n && A[j]==A[0]){
            j++;
        }
        if(j==n){
            return true;
        }
        if(A[j]>A[0]){
            while(j+1<n &&  A[j+1]>=A[j]){
                j++;
            }
        }else{
            while(j+1<n &&  A[j+1]<=A[j]){
                j++;
            }
            
        }
        if( j+1 == n){
            return true;
        }
        return false;

        
    }
    public static void main(String args[]) {
        int[] nums = new int[] { 1,2,2,3};
        System.out.println("Result = " + isMonotonic(nums));
    }
}
