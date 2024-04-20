class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visited = set()
        rows = len(land)
        cols = len(land[0])
        ans = []
        def getBounds(i, j):
            curri = i
            currj = j
            while curri<rows and land[curri][j]==1:
                curri+=1
            curri-=1
            while currj<cols and land[i][currj]==1:
                currj+=1
            currj-=1
            return [i, j, curri, currj]
        for i in range(rows):
            for j in range(cols):
                if land[i][j]==1:
                    if i>0:
                        if land[i-1][j]==1:
                            continue
                    if j>0:
                        if land[i][j-1]==1:
                            continue
                    ans.append(getBounds(i, j))
        return ans