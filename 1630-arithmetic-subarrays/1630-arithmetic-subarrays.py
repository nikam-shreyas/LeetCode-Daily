class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for left, right in zip(l, r):
            seq = nums[left:right+1]
            seq.sort()
            diff = seq[1]-seq[0]
            flag = True
            for i in range(2, len(seq)):
                if diff!=seq[i]-seq[i-1]:
                    flag = False
                    break
            ans.append(flag)
        return ans