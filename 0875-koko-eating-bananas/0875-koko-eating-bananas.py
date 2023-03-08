class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low = 1
        high = piles[-1]
        while low<=high:
            def checkValid(mid):
                f = 0
                for p in piles:
                    f+=ceil(p/mid)
                    if f>h:
                        return False
                return f<=h
            mid = low+(high-low)//2
            if checkValid(mid):
                high=mid-1
            else:
                low=mid+1
        return low