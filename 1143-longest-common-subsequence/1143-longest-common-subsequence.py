class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n =  len(text1)
        m = len(text2)
        
        dp = []
        for _ in range(n):
            dp.append( [0]*(m))
        
        dp[0][0]= 1 if text1[0]==text2[0] else 0
        
        for i in range(1,n):
            dp[i][0] = dp[i-1][0]
            if text1[i]==text2[0]:
                dp[i][0] = max(dp[i][0],1)
                
        for i in range(1,m):
            dp[0][i]=dp[0][i-1]
            if text1[0]==text2[i]:
                dp[0][i] = max(dp[0][i],1)
                
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if text1[i]==text2[j]:
                    dp[i][j] = max(dp[i][j],1+dp[i-1][j-1])
                
        
        # for row in dp:
        #     print(row)
            
        return dp[-1][-1]