class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recurse(i, j, ptillnow):
            if i==0 and j==0:
                ans.append(ptillnow)
                return
            if i==0:
                while j>0:
                    ptillnow+=')'
                    j-=1
                ans.append(ptillnow)
                return
            else:
                recurse(i-1, j, ptillnow+'(')
                if i<j:
                    recurse(i, j-1, ptillnow+')')
        recurse(n, n, '')
        return ans
                