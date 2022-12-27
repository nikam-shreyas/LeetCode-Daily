class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], ar: int) -> int:
        diff = sorted([x-y for x, y in zip(capacity, rocks)])
        count = 0
        for d in diff:
            if ar-d>=0:
                ar-=d
                count+=1
            else:
                break
        return count
            