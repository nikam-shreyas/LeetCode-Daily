class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(i, j, index, visited):
            if index==len(word):
                return True
            if i<0 or j<0 or i>=rows or j>=cols or (i, j) in visited:
                return False
            if board[i][j]!=word[index]:
                return False
            ans = False
            visited_copy = visited.copy()
            visited_copy.add((i, j))
            return dfs(i+1, j, index+1, visited_copy) or dfs(i-1, j, index+1, visited_copy) or dfs(i, j+1, index+1, visited_copy) or dfs(i, j-1, index+1, visited_copy)
                
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    visited = set()
                    if dfs(i, j, 0, visited):
                        return True
        return False
            