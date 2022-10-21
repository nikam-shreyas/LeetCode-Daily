class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        if k==0:
            return False
        for i in range(min(len(nums), k)):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        # print(s)
        for i in range(min(k, len(nums)), len(nums)):
            # print(s, nums[i])
            if nums[i] in s:
                return True
            s.remove(nums[i-k])
            s.add(nums[i])
        return False