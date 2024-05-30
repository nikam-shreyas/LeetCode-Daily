class Solution:
    def numSteps(self, s: str) -> int:
        decimal_number = 0
        pow_of_2 = 0
        for i in range(len(s)-1, -1, -1):
            decimal_number += (ord(s[i])-ord('0'))*(pow(2, pow_of_2))
            pow_of_2+=1
        count = 0
        while decimal_number!=1:
            if decimal_number%2==0:
                decimal_number = decimal_number // 2
            else:
                decimal_number += 1
            count+=1
        return count
            