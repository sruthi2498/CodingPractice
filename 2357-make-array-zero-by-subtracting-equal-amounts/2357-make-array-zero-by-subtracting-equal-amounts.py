class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        toSubtract = 0
        while i<n and nums[i]==0:
            i+=1
            
        count = 0
        while i<n:
            if nums[i]-toSubtract>0:
                toSubtract+=(nums[i]-toSubtract)
                count+=1
            i+=1
        return count