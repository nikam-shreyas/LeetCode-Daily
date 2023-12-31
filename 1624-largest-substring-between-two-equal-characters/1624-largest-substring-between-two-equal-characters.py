class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ht = {}
        maxlen = -1
        for i, char in enumerate(s):
            if char in ht:
                maxlen = max(maxlen, i-ht[char]-1)
            else:
                ht[char] = i
        return maxlen
                