class Solution:
    def checkString(self, s: str) -> bool:
        s = list(s)
        return s==sorted(s)