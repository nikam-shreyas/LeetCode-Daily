class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {}
        modu = pow(10, 9)+7
        def recurse(curlen):
            if curlen in dp:
                return dp[curlen]
            if low<=curlen<=high:
                dp[curlen] = 1+recurse(curlen+zero)%modu+recurse(curlen+one)%modu
            elif curlen>high:
                return 0
            else:
                dp[curlen] = recurse(curlen+zero)%modu+recurse(curlen+one)%modu
            return dp[curlen]%modu
        return recurse(0)%modu