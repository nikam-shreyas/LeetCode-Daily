class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                ans.append((i+j, j, nums[i][j]))
        ans.sort()
        res = []
        for _, _, val in ans:
            res.append(val)
        return res
        