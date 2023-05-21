class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        n, total, dict1 = len(nums), 0, collections.Counter(x&y for x in nums for y in nums)

        for i in nums:
            for j in dict1:
                if i&j == 0:
                    total += dict1[j]

        return total