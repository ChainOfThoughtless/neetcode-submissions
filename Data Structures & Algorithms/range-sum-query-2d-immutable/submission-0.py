class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.R = len(matrix)
        self.C = len(matrix[0])
        self.sumMat = [[0] * (self.C + 1) for _ in range(self.R + 1)]
        for r in range(self.R):
            for c in range(self.C):
                self.sumMat[r + 1][c + 1] = matrix[r][c] + self.sumMat[r][c + 1] + self.sumMat[r + 1][c] - self.sumMat[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.sumMat[row2 + 1][col2 + 1]
        subtraction = self.sumMat[row2 + 1][col1] + self.sumMat[row1][col2 + 1] - self.sumMat[row1][col1]
        return total - subtraction


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)