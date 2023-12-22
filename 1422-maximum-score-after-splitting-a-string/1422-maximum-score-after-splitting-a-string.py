class Solution:
    def maxScore(self, s: str) -> int:
        zeroCount = 0
        oneCount = 0
        for char in s:
            if char=='1':
                oneCount+=1
        maxSum = 0
        if s[0]=='1':
            oneCount-=1
        if s[0]=='0':
            zeroCount+=1
        for i in range(1, len(s)-1):
            maxSum = max(maxSum, oneCount+zeroCount)
            char = s[i]
            if char=='1':
                oneCount-=1
            else:
                zeroCount+=1
        maxSum = max(maxSum, oneCount+zeroCount)
        return maxSum
                