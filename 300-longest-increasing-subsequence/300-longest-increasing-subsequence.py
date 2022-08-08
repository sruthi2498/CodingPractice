class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n
        maxLis = 1
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j]+1
                    if lis[i]>maxLis:
                        maxLis = lis[i]

        return maxLis