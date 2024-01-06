class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(s,e,p) for s,e,p in sorted(zip(startTime, endTime, profit))]
        minHeap = [] # tuple(end time, max profit ending at this job)
        maxProfit = 0

        for s,e,p in jobs:
            # pop all jobs with end time before cur start time (s) to update max profit up until s.
            while minHeap and minHeap[0][0] <= s:
                _, prevProfit = heappop(minHeap)
                maxProfit = max(maxProfit, prevProfit)
            # add next job to heap with added profit.
            heappush(minHeap, (e, maxProfit + p))
        
        return max(minHeap, key=lambda x: x[1])[1]