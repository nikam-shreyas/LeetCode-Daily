class Solution:
    def average(self, salary: List[int]) -> float:
        n = 0
        maxs = -inf
        mins = inf
        sums = 0
        for s in salary:
            n+=1
            sums+=s
            maxs=max(maxs, s)
            mins = min(mins, s)
        return (sums - maxs - mins) / (n-2)
            
        