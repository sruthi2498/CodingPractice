class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[-1])
        i = n-2
        while i>=0:
            print(triangle[i])
            for j in range(0,i+1):
                triangle[i][j] = min(triangle[i][j]+triangle[i+1][j], triangle[i][j]+triangle[i+1][j+1])
            print(triangle[i])
            
            i-=1
        return triangle[0][0]