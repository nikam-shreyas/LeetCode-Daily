class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target<n or target>(k*n):
            return 0
        modu = pow(10, 9)+7
        dp = {}
        def recurse(rem_sum, rem_die):
            if (rem_sum, rem_die) in dp:
                return dp[(rem_sum, rem_die)]
            if (rem_sum<0) or (rem_die>0 and rem_sum==0):
                dp[(rem_sum, rem_die)] = 0
                return 0
            elif (rem_sum==0 and rem_die==0) or (rem_die==1 and 0<rem_sum<=k):
                dp[(rem_sum, rem_die)] = 1
                return 1
            else:
                s=0
                for i in range(1, k+1):
                    s+=recurse(rem_sum-i, rem_die-1)%modu
                dp[(rem_sum, rem_die)] = s
                return s
        return recurse(target, n)%modu