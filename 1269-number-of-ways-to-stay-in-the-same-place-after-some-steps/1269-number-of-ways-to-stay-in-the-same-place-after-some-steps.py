class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # def recurse(rem_steps, curr_pos):
        #     if curr_pos>=arrLen or curr_pos<0:
        #         return 0
        #     if curr_pos==0 and rem_steps==0:
        #         return 1
        #     if rem_steps==0 and curr_pos!=0:
        #         return 0
        #     return recurse(rem_steps-1, curr_pos-1)+recurse(rem_steps-1, curr_pos+1)+recurse(rem_steps-1, curr_pos)
        # return recurse(steps, 0)
        modu = pow(10, 9)+7
        dp = [0 for _ in range(arrLen)]
        dp[0] = 1
        arrLen = min(steps, arrLen)
        for i in range(steps):
            temp = []
            # print(dp)
            for j in range(arrLen):
                temp.append(dp[j])
                if j>0:
                    temp[-1]+=dp[j-1]%modu
                if j<arrLen-1:
                    temp[-1]+=dp[j+1]%modu
            dp = temp
        # print(dp)
        # print()
        return dp[0]%modu