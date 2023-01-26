class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        if n<=1:
            return n
        elif n==2:
            return 1
        t3 = t0+t2+t1
        while n-3:
            t0 = t1
            t1 = t2
            t2 = t3
            t3 = t1+t2+t0
            n-=1
        return t3