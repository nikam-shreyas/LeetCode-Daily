class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = Counter(s)['1']
        ans = ['0']*len(s)
        for i in range(ones-1):
            ans[i]='1'
        ans[-1]='1'
        return ''.join(ans)