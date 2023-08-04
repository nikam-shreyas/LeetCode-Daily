class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s = list(s)
        dp = {}
        def recurse(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j>len(s) or i>j:
                return False
            if j==len(s):
                if ''.join(s[i:j]) in wordDict:
                    return True
            if ''.join(s[i:j]) in wordDict:
                dp[(i, j)] = recurse(j, j+1) or recurse(i, j+1)
                return dp[(i, j)]
            else:
                dp[(i, j)] = recurse(i, j+1)
                return dp[(i, j)]
        return recurse(0, 0)