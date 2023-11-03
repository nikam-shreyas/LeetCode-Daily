class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        j = 1
        ans = []
        while i<len(target) and j<=n:
            if target[i]==j:
                ans.append("Push")
                i+=1
            else:
                ans.append("Push")
                ans.append("Pop")
            j+=1
        return ans