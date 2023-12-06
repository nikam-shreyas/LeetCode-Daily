class Solution:
    def totalMoney(self, n: int) -> int:
        amount = 0
        start = 1
        temp = start
        for i in range(1, n+1):
            amount+=temp
            if i%7==0:
                temp = start
                start+=1
            temp+=1
            # n-=1
        return amount
        