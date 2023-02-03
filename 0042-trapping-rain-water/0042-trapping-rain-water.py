class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lheight = [0 for _ in range(n)]
        rheight = [0 for _ in range(n)]
        lheight[0] = height[0]
        rheight[n-1] = height[n-1]
        for i in range(1,n):
            lheight[i]=max(lheight[i-1], height[i])
            rheight[n-1-i]=max(rheight[n-1-i+1], height[n-1-i])
        ans = 0
        for i in range(n):
            ans+=max(min(lheight[i], rheight[i])-height[i], 0)
        return ans