class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        opt = []
        for _ in range(n):
            opt.append([False]*n)
            
        for i in range(n):
            opt[i][i] = True 
            
        
        '''
        01 12 23 34
        02 13 24
        03 14
        04
        '''
        for i in range(1,n):
            for j in range(n-i):
                # print(j,j+i)
                k = j
                l = j+i
                if i == 1:
                    opt[k][l] = True if s[k]==s[l] else False
                else:
                    opt[k][l] = True if (s[k]==s[l] and opt[k+1][l-1]) else False
        # for row in opt:
        #     print(row)
        
        maxP = s[0]
        maxLen = 1
        for i in range(1,n):
            for j in range(n-i):
                k = j
                l = j+i
                if opt[k][l]:
                    if i+1 > maxLen :
                        maxLen = i+1
                        maxP = s[k:l+1]
        return maxP
                    