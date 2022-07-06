class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [0]
        n = len(nums)
        for i in range(1,n):
            leftSum.append(leftSum[i-1]+nums[i-1])
        # print(leftSum)
        rightSum = [0]
        for i in range(n-2,-1,-1):
            rightSum.append(rightSum[n-i-2]+nums[i+1])
        rightSum.reverse()
        # print(rightSum)
        i = 0
        while i<n:
            if leftSum[i]==rightSum[i]:
                return i
            i+=1
        return -1