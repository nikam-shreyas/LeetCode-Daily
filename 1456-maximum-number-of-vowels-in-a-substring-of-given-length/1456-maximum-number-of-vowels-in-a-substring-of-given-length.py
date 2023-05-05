class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelcount = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        maxcount = -1
        for i in range(k):
            if s[i] in vowels:
                vowelcount+=1
                maxcount=max(maxcount, vowelcount)
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                vowelcount-=1
            if s[i] in vowels:
                vowelcount+=1
                maxcount = max(maxcount, vowelcount)
        return max(0, maxcount)