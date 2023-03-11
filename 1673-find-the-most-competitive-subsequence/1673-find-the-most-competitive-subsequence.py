class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i]<st[-1]:
                while k-len(st)<len(nums)-i and st and st[-1]>nums[i]:
                    st.pop()
                st.append(nums[i])
            elif len(st)<k:
                st.append(nums[i])
        return st
                
                    