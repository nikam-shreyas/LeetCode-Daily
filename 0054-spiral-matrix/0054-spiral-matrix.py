class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = cols-1
        up = 0
        down = rows-1
        visited = set()
        ans = []
        count = 0
        def goright(r, left, right):
            nonlocal count
            for i in range(left, right+1):
                ans.append(matrix[r][i])
                count+=1
        def godown(c, up, down):
            nonlocal count
            for i in range(up, down+1):
                ans.append(matrix[i][c])
                count+=1
        def goleft(r, right, left):
            nonlocal count
            for i in range(right, left-1, -1):
                ans.append(matrix[r][i])
                count+=1
        def goup(c, down, up):
            nonlocal count
            for i in range(down, up-1, -1):
                ans.append(matrix[i][c])
                count+=1
                
        while count<(rows*cols):
            goright(up, left, right)
            up+=1
            
            godown(right, up, down)
            right-=1
            
            goleft(down, right, left)
            down-=1
            
            goup(left, down, up)
            left+=1
            
        return ans[:(rows*cols)]