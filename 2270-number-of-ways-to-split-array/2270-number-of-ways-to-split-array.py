class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [nums[0]]
        for i in range(1,n):
            prefixSum.append(nums[i]+prefixSum[i-1])
        count = 0
        for i in range(n-1):
            if prefixSum[i]>=prefixSum[n-1]-prefixSum[i]:
                count+=1
        return count