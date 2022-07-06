class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i = 1
        while i<len(nums):
            nums[i]+=nums[i-1]
            i+=1
        i = 0
        while i<len(nums):
            leftSum = 0 if i==0 else nums[i-1]
            if leftSum==nums[-1] - nums[i]:
                return i
            i+=1
        return -1