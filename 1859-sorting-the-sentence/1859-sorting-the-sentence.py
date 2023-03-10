class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        ans = ['' for _ in range(len(s))]
        for word in s:
            ans[int(word[-1])-1]=word[:-1]
        return ' '.join(ans)
            