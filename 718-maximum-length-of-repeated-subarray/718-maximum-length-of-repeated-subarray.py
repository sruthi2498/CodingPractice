class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [ [0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1 if nums1[0]==nums2[0] else 0
        for j in range(1,m):
            if nums2[j]==nums1[0]:
                 dp[0][j] = 1 
        for i in range(1,n):
            if nums1[i]==nums2[0]:
                 dp[i][0] = 1 
            
        for i in range(1,n):
            for j in range(1,m):
                if nums1[i]==nums2[j]:
                    dp[i][j] = 1+dp[i-1][j-1]
                    
        result = 0
        for row in dp:
            result = max(result,max(row))
            # print(row)
            
        return result