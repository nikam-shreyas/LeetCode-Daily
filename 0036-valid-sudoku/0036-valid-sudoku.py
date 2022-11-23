class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s1 = set()
            s2 = set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in s1:
                        return False
                    else:
                        s1.add(board[i][j])
                if board[j][i]!='.':
                    if board[j][i] in s2:
                        return False
                    else:
                        s2.add(board[j][i])
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                s = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l]!='.':
                            if board[i+k][j+l] in s:
                                return False
                            else:
                                s.add(board[i+k][j+l])
        return True
                    
                
                
                