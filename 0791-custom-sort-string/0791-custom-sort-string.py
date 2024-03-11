class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hm = {}
        for char in s:
            if char in hm:
                hm[char]+=1
            else:
                hm[char]=1
        ans = []
        s = set()
        for char in order:
            if char in hm:
                s.add(char)
                ans.extend([char]*hm[char])
        for k in hm.keys():
            if k not in s:
                ans.extend([k]*hm[k])
        return ''.join(ans)
            