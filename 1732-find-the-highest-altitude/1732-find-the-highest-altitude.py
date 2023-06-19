class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        sumsofar = 0
        for height in gain:
            sumsofar+=height
            highest = max(highest, sumsofar)
        return highest