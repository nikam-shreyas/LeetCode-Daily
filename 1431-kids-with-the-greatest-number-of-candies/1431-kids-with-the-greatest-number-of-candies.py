class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxval = max(candies)
        res = []
        for candy in candies:
            if candy+extraCandies>=maxval:
                res.append(True)
            else:
                res.append(False)
        return res