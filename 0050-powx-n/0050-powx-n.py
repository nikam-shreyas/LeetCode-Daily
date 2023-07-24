class Solution:
    @lru_cache
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x, -n)
        if n==1:
            return x
        if n%2==0:
            return self.myPow(x, n//2)*self.myPow(x, n//2)
        else:
            return x*self.myPow(x, (n-1)//2)*self.myPow(x, (n-1)//2)
        
        
        