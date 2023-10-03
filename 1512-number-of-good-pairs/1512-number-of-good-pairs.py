class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i]==nums[j]:
        #             count+=1
        # return count
        d_occurrences = {}
        for num in nums:
            if num in d_occurrences:
                count+=d_occurrences[num]
                d_occurrences[num]+=1
            else:
                d_occurrences[num]=1
        return count