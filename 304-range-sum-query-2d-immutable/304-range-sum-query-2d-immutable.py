class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.rowPrefixSumMat = []
        self.calculatePrefixSum()
        
    def calculatePrefixSum(self):
        
        for i in range(self.n):
            row = [self.matrix[i][0]]
            for j in range(1,self.m):
                row.append(self.matrix[i][j]+row[j-1])
            self.rowPrefixSumMat.append(row)
        # for row in self.rowPrefixSumMat:
        #     print(row)
    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1,row2+1):
            s = self.rowPrefixSumMat[i][col2]-self.rowPrefixSumMat[i][col1-1] if col1>0 else self.rowPrefixSumMat[i][col2]
            res+=s
        return res
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)