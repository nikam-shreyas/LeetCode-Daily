class Solution:
    def minOperations(self, nums: List[int]) -> int:
        minOps = 0
        for num in Counter(nums).values():
            if num==1:
                return -1
            minOps+=ceil(num/3)
        return minOps