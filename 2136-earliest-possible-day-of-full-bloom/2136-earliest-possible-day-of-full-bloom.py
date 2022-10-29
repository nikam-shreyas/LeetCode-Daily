import functools
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plants = list(zip(growTime, plantTime))
        plants.sort(reverse=True)
        ltime, rtime = 0, 0
        for end, start in plants:
            ltime+=start
            rtime=max(ltime+end, rtime)
        return max(ltime, rtime)
        