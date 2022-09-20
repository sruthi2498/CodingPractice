class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            prefixSum.append(nums[i]+prefixSum[i-1])
        print(prefixSum)
        if prefixSum[-1]<target:
            return 0
        i = 0
        while i<n and prefixSum[i]<target:
            i+=1
            
        j = 0
        bestWindow = i-j+1
        while j<n and i<n:
            print("i = ",i," j = ",j)
            currSum = prefixSum[i]-prefixSum[j]
            while currSum>target and j<=i:
                j+=1
                currSum = prefixSum[i]-prefixSum[j]
            windowSize = i-j+1
            if currSum>=target:
                windowSize-=1
            bestWindow = min(bestWindow,windowSize)
            i+=1
        return bestWindow
            
        print(i)