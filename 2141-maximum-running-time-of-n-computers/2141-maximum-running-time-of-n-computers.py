from heapq import heapify, heappush, heappop
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        minTime = 1
        maxTime = sum(batteries)//n
        
        while minTime<maxTime:
            midTime = maxTime - (maxTime-minTime)//2
            supply = 0
            for battery in batteries:
                supply+=min(battery, midTime)
            
            if supply // n >= midTime:
                minTime = midTime
            else:
                maxTime = midTime-1
                
        return minTime