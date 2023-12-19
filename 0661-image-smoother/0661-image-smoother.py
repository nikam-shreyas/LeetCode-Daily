import numpy as np
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        img = np.array(img)
        r, c = img.shape
        ans = np.zeros((img.shape), dtype=int)
        
        for i in range(r):
            for j in range(c):
                s = 0
                for k in range(max(0, i-1), min(i+2, r)):
                    s+=sum(img[k][max(0, j-1):min(j+2, c)])
                n = ((min(i+2, r)-max(0, i-1))*(min(j+2, c) - max(0, j-1)))
                ans[i][j] = int(floor(s/n))
        return ans