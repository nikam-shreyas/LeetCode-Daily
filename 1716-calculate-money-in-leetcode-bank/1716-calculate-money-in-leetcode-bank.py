class Solution:
    def totalMoney(self, n: int) -> int:
        # amount = 0
        # start = 1
        # temp = start
        # for i in range(1, n+1):
        #     amount+=temp
        #     if i%7==0:
        #         temp = start
        #         start+=1
        #     temp+=1
        #     # n-=1
        # return amount
        num_completed_weeks = n//7
        amount=num_completed_weeks*28
        amount+=((num_completed_weeks-1)*(num_completed_weeks))//2*7
        remaining_days = n%7
        amount+=(remaining_days*(remaining_days+1)//2)+(num_completed_weeks*remaining_days)
        return amount
        