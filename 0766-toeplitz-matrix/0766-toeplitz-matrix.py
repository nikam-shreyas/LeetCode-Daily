class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        def check(i, j, val):
            if not (0<=i<r and 0<=j<c):
                return True
            if not matrix[i][j]==val:
                return False
            return check(i+1, j+1, val)
        for col in range(c):
            if not check(0, col, matrix[0][col]):
                return False
        for row in range(r):
            if not check(row, 0, matrix[row][0]):
                return False
        return True