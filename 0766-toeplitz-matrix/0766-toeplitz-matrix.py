class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        for col in range(c):
            i = 0
            j = col
            val = matrix[i][j]
            while i<r and j<c:
                if matrix[i][j]!=val:
                    return False
                i+=1
                j+=1
        for row in range(r):
            i = row
            j = 0
            val = matrix[i][j]
            while i<r and j<c:
                if matrix[i][j]!=val:
                    return False
                i+=1
                j+=1
        return True