class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        dp = {}
        events.sort()
        def recurse(currend, curri, k):
            if (currend, curri, k) in dp:
                return dp[(currend, curri, k)]
            if k==0 or curri==len(events):
                return 0
            
            temp = 0
            if events[curri][0]>currend:
                temp = events[curri][2]+recurse(events[curri][1], curri+1, k-1)
            
            temp = max(temp, recurse(currend, curri+1, k))
            dp[(currend, curri, k)]=temp
            return temp
        
        return recurse(0, 0, k)