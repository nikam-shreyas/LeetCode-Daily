class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k_: int) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        answer = [[0 for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                sum_ = 0
                for k in range(max(0, i-k_), min(r, i+k_+1)):
                    for l in range(max(0, j-k_), min(c, j+k_+1)):
                        sum_+=mat[k][l]
                answer[i][j]=sum_
        return answer