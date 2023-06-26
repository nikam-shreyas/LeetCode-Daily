class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = 0
        right = len(costs)-1
        score = 0
        temp = candidates
        pool = []
        heapq.heapify(pool)
        while left<=right and temp>0:            
            heapq.heappush(pool, (costs[left], left))
            temp-=1
            left+=1
        temp = candidates
        while left<=right and temp>0:
            heapq.heappush(pool, (costs[right], right))
            right-=1
            temp-=1
        # print(pool)
        while left<=right:
            # print(pool)
            curr, pos = heapq.heappop(pool)
            score+=curr
            if pos<=left:
                heapq.heappush(pool, (costs[left], left))
                left+=1
            else:
                heapq.heappush(pool, (costs[right], right))
                right-=1
            k-=1
            if k==0:
                break
        while k>0:
            # print(pool)
            curr, pos = heapq.heappop(pool)
            score+=curr
            k-=1
        return score