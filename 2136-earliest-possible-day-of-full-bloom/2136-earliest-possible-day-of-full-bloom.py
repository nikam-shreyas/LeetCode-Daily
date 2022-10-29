import functools
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        def compare(x, y):
            if x[1]==y[1]:
                return x[0]<y[0]
            return x[1]<y[1]
        plants = list(zip(growTime, plantTime))
        plants.sort(reverse=True)
        ltime, rtime = 0, 0
        for end, start in plants:
            ltime+=start
            rtime=max(ltime+end, rtime)
        return max(ltime, rtime)
        