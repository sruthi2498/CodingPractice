class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        coins.sort()
        n = len(coins)
        
        # opt[i][j] = num of coins till coins[i] needed to make amount j
       
        opt = []
        for i in range(n):
            opt.append([math.inf for j in range(amount+1)])
            
        for i in range(n):
            opt[i][0] = 0
            
        for j in range(coins[0],amount+1):
            if opt[0][j-coins[0]]!=math.inf:
                opt[0][j] = 1+opt[0][j-coins[0]]
        
        for i in range(1,n):
            for j in range(1, amount+1):
                opt[i][j] = opt[i-1][j]
                if j>=coins[i] and opt[i][j-coins[i]]!=math.inf:
                    # print(j,coins[i],opt[i][j-coins[i]])
                    opt[i][j] = min( opt[i][j],1+opt[i][j-coins[i]] )
        # print()       
        # for row in opt:
        #     print(row)
        return opt[-1][-1] if opt[-1][-1]< math.inf else  -1
            
            
                
        