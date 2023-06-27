from heapq import heapify, heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = []
        heap = []
        heapify(heap)
        heappush(heap, (nums1[0]+nums2[0], 0, 0))
        visited = set([0, 0])
        while k and heap:
            value, i, j = heappop(heap)
            pairs.append([nums1[i], nums2[j]])
            if i+1<len(nums1) and (i+1, j) not in visited:
                visited.add((i+1, j))
                heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
            if j+1<len(nums2) and (i, j+1) not in visited:
                visited.add((i, j+1))
                heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            k-=1
        return pairs
            
                
            