class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
        
        
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                if matrix[i][j]:
                    matrix[i][j] = 1 + min(matrix[i+1][j],matrix[i][j+1],matrix[i+1][j+1])
        
        maxVal = 0
        for i in range(n):
            for j in range(m):
                maxVal = max(matrix[i][j] ,maxVal)
        return maxVal**2