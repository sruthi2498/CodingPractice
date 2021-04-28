package arrays;

// 11. https://leetcode.com/problems/container-with-most-water/submissions/
public class MaxAreaWater {
    public static int maxArea(int[] height) {
        int l = 0;
        int r = height.length - 1;
        int maxArea = 0;
        int minH;
        int diff = r - l;
        while (l < r) {
            minH = height[l] <= height[r] ? height[l] : height[r];
            maxArea = minH * diff > maxArea ? minH * diff : maxArea;
            if (height[l] <= height[r]) {
                l += 1;
            } else {
                r -= 1;
            }
            diff -= 1;
        }
        return maxArea;

    }

    public static void main(String args[]) {
        int[] nums = new int[] { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
        System.out.println("Result = " + maxArea(nums));
    }
}
