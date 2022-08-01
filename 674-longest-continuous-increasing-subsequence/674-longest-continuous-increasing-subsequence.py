class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxLen = 1
        i = 0
        n = len(nums)
        while i<n:
            j = i+1
            while j<n and nums[j]>nums[j-1]:
                j+=1
            maxLen = max(maxLen, j-i)
            i = j
        return maxLen