import math
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # if n<=2:
        #     return 0
        maxElem = nums[0]
        end = 0
        for i in range(n):
            # print(maxElem,nums[i],end)
            if maxElem > nums[i]:
                end = i
            else:
                maxElem = nums[i]
        # print(end)
        start = n-1
        minElem = nums[start]
        for i in range(n-1, -1, -1):
            if minElem < nums[i]:
                start = i
            else:
                minElem = nums[i]
        print(start)
        if end != 0:
            return end - start + 1
        else: 
            return 0
        