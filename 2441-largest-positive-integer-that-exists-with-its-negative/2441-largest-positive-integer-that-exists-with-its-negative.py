class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set()
        maxnum = -1
        for num in nums:
            if -num in s:
                maxnum = max(maxnum, abs(num))
            else:
                s.add(num)
        return maxnum
            