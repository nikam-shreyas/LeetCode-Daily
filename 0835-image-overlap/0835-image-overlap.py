import numpy as np
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        padding = n*2
        total_size = padding+n
        img2_copy = np.zeros((total_size,total_size))
        img2_copy[n-1:2*n-1, n-1:2*n-1]=img2
        largest_overlap = 0
        img1 = np.array(img1)
        # print(img2_copy)
        for i in range(total_size-n):
            for j in range(total_size-n):
                icopy = img2_copy[i:i+n, j:j+n]
                res = np.logical_and(img1, icopy)
                largest_overlap = max(largest_overlap, np.sum(res))
        return largest_overlap