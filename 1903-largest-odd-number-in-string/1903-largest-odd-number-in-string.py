class Solution:
    def largestOddNumber(self, num: str) -> str:
        j = len(num)-1
        while j>=0 and int(num[j])%2==0:
            j-=1
        if j==-1:
            return ""
        else:
            return num[:j+1]