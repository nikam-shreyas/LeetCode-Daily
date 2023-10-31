class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        prev_xor = pref[0]
        for i in range(1, len(pref)):
            temp = pref[i]^prev_xor
            ans.append(temp)
            prev_xor = prev_xor^ans[-1]
        return ans