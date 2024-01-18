class Solution:
    dp={0:1}
    
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        last = first+second
        if n<=2:
            return n
        for i in range(3, n):
            first = second
            second = last
            last = first+second
        return last