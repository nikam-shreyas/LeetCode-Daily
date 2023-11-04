class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = -1
        for i in left:
            ans=max(ans, i)
        for j in right:
            ans = max(ans,n-j)
        return ans