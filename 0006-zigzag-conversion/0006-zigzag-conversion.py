class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        # print(ans)
        i=0
        k=0
        while True:
            if i>=len(s):
                break
            j=0
            while i<len(s) and j<numRows:
                # print(i, j, ans)
                ans[j].append(s[i])
                j+=1
                i+=1
            j-=2
            while i<len(s) and j>0:
                # print(i, j, ans)
                ans[j].append(s[i])
                i+=1
                j-=1
            # print(ans)
        res = ''
        # print(ans)
        for i in ans:
            res+=''.join(i)
        return res