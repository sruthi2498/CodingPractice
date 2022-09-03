class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        opt = []
        for _ in range(n):
            opt.append([math.inf]*m)
        for j in range(m):
            opt[0][j] = grid[0][j]
            
#         for row in opt:
#             print(row)
            
        for i in range(1,n):
            for j in range(m):
                for k in range(m):
                    opt[i][j] = min(opt[i][j], 
                                   opt[i-1][k] + moveCost[grid[i-1][k]][j]
                                   + grid[i][j])
        # for row in opt:
        #     print(row)
        result = math.inf    
        for j in range(m):
            result = min(result, opt[-1][j])
            
        return result