class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        count = 0
        for i in range(cols):
            for j in range(1, rows):
                if ord(strs[j][i])<ord(strs[j-1][i]):
                    count+=1
                    break
        return count