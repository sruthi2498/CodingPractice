import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        grid = np.array(grid)
        rowMax = [max(row) for row in grid]
        colMax = [max(grid[:,i]) for i in range(len(grid))]
        print(rowMax,colMax)
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                diff = min(rowMax[i],colMax[j]) - grid[i][j]
                total+=diff
        return total