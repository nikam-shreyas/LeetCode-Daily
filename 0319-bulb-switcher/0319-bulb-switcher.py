class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulbs = 0
        i=1
        while i*i<=n:
            i+=1
            bulbs+=1
        return bulbs
        