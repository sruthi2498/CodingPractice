class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        if n==1 :
            return 1 if not mines else 0
        if n==2:
            return 1 if len(mines)<4 else 0
        grid = []
        for i in range(n):
            grid.append([1]*n)
        for i,j in mines:
            grid[i][j] = 0
        for row in grid:
            print(row)
            
        counts = []
        for i in range(n):
            counts.append([[0,0,0,0] for _ in range(n)])
            
        for i in range(n):
            if grid[i][0]:
                counts[i][0][0] = 1 #left
            if grid[i][n-1]:
                counts[i][n-1][2] = 1 #right
        for i in range(n):
            if grid[0][i]:
                counts[0][i][1] = 1 #top
            if grid[n-1][i]:
                counts[n-1][i][3] = 1 #bot
        
            
        #left
        for i in range(n):
            for j in range(1,n):
                if grid[i][j]:
                    counts[i][j][0] = counts[i][j-1][0] + grid[i][j]
                    
        #top
        for i in range(1,n):
            for j in range(n):
                if grid[i][j]:
                    counts[i][j][1] = counts[i-1][j][1] + grid[i][j]
                    
        #right
        for i in range(n):
            for j in range(n-2,-1,-1):
                if grid[i][j]:
                    counts[i][j][2] = counts[i][j+1][2] + grid[i][j]
                    
        #bot
        for i in range(n-2,-1,-1):
            for j in range(n):
                if grid[i][j]:
                    counts[i][j][3] = counts[i+1][j][3] + grid[i][j]
        
        
        # for row in counts:
        #     print(row)
            
        maxOrder = 1 
        for i in range(1,n-1):
            for j in range(1,n-1):
                if grid[i][j]:
                    arms = min(counts[i-1][j][1], counts[i][j-1][0], counts[i][j+1][2] , counts[i+1][j][3] )
                    order = 1 + arms if arms else 0
                    maxOrder = max(maxOrder,order)
                    # print(i,j,order)
                
        return maxOrder
                    
                    
                    
                    
                    
                    
                