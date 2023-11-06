from heapq import heapify, heappush, heappop
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        score = 0
        cur = arr[0]
        for i in range(1, n):
            if arr[i] < cur:
                score += 1
            else:
                if score >= k:
                    return cur
                cur = arr[i]
                score = 1
        
        return cur
                
        
        