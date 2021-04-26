package arrays;

import java.util.Arrays;

// 33 https://leetcode.com/problems/search-in-rotated-sorted-array/
public class SearchInSortedArray {
    public static int findMinIndex(int[] nums) {
        if (nums.length == 1) {
            return 0;
        }
        int i = 0;
        while ((i + 1) < nums.length && nums[i + 1] > nums[i]) {
            i++;
        }
        if (i + 1 == nums.length) {
            return 0;
        }
        return i + 1;
    }

    public static int binarySearchIndexResult(int[] nums, int target, int l, int r) {

        int mid;
        while (l >= 0 && l < nums.length && r >= 0 && r < nums.length) {

            if (target < nums[l] || target > nums[r]) {
                return -1;
            }
            if (target == nums[l]) {
                return l;
            }
            if (target == nums[r]) {
                return r;
            }

            mid = l + (r - l + 1) / 2;

            if (target == nums[mid]) {
                return mid;
            }

            if (target >= nums[l] && target <= nums[mid]) {
                if (r == mid) {
                    return -1;
                }
                r = mid;
            } else if (target > nums[mid] && target <= nums[r]) {
                if (l == mid) {
                    return -1;
                }
                l = mid;
            }
        }
        return 0;
    }

    public static int search(int[] nums, int target) {
        // this.nums = nums;
        int minIndex = findMinIndex(nums);

        if (minIndex == 0) {
            return binarySearchIndexResult(nums, target, 0, nums.length - 1);
        } else {
            if (target >= nums[minIndex] && target <= nums[nums.length - 1]) { // second half
                return binarySearchIndexResult(nums, target, minIndex, nums.length - 1);

            } else {
                return binarySearchIndexResult(nums, target, 0, minIndex - 1);

            }
        }

    }

    public static void main(String args[]) {
        int[] nums = new int[] { 1, 2, 4 };
        int target = 3;
        System.out.println("Result = " + search(nums, target));
    }
}
