class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        r = len(grid)
        c = len(grid[0])
        ans = []
        for col in range(c):
            row = 0
            curr_col = col
            # print()
            while row<=r:
                # print(row, curr_col)
                if row==r:
                    ans.append(curr_col)
                    break
                elif curr_col==-1 or curr_col==c:
                    ans.append(-1)
                    break
                else:
                    curr_val = grid[row][curr_col]
                    if curr_val>0:
                        if curr_col+1<c and grid[row][curr_col+1]>0:
                            curr_col+=1
                        else:
                            curr_col=-1
                    else:
                        if curr_col-1>=0 and grid[row][curr_col-1]<0:
                            curr_col-=1
                        else:
                            curr_col=-1
                row+=1
        return ans