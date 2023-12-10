class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        ans = [[0 for _ in range(r)] for _ in range(c)]
        for i in range(r):
            for j in range(c):
                ans[j][i] = matrix[i][j]
        return ans