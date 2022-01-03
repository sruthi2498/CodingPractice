class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = []
        for i in range(n):
            dp.append([0]*2)
        # for row in dp:
        #     print(row)
        if nums[0]==0:
            dp[0][0] = 0
        else:
            dp[0][0] = 1
        for i in range(1,n):
            if nums[i]:
                dp[i][0]=dp[i-1][0]+1
                dp[i][1] = dp[i-1][1]+1
            else:
                dp[i][0]=0
                dp[i][1]=dp[i-1][0]
        max_val = 0
        for i in range(n):
            if dp[i][1]>max_val:
                max_val = dp[i][1]
        return max_val
                
            