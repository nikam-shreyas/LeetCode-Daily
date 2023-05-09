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
            
                
        while count<(rows*cols):
            for i in range(left, right+1):
                ans.append(matrix[up][i])
                count+=1
            up+=1
            
            for i in range(up, down+1):
                ans.append(matrix[i][right])
                count+=1
            right-=1
            
            for i in range(right, left-1, -1):
                ans.append(matrix[down][i])
                count+=1
            down-=1
            
            for i in range(down, up-1, -1):
                ans.append(matrix[i][left])
                count+=1
            left+=1
            
        return ans[:(rows*cols)]