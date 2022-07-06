class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        i = 1
        n = len(nums)
        while i<n:
            prefixSum.append(prefixSum[i-1]+nums[i])
            i+=1
        print(prefixSum)
        i = 0
        while i<n:
            leftSum = 0 if i==0 else prefixSum[i-1]
            rightSum = prefixSum[-1] - prefixSum[i]
            if leftSum==rightSum:
                return i
            i+=1
        return -1