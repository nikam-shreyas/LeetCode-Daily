class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        i=0
        modu = pow(10,9)+7
        ans = []
        while n>0:
            if n%2==1:
                ans.append(pow(2, i))
            n=n//2
            i+=1
        # print(ans)
        res = []
        for i, j in queries:
            temp = 1
            for k in range(i, j+1):
                temp=(temp*ans[k])%modu
            res.append(temp)
        return res
                