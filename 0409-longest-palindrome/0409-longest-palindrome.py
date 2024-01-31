class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        evens = 0
        maxodds = 0
        flag = False
        for item, val in counter.items():
            if val%2==0:
                evens+=val
            else:
                flag = True
                maxodds+=val-1
        return evens+maxodds+1 if flag else evens+maxodds