class Solution:
    def isPalindrome(self, x: int) -> bool:
        return list(str(x))==list(reversed(list(str(x))))