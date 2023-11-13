class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        ans = []
        vowels_in_s = []
        for c in s:
            if c in vowels:
                vowels_in_s.append(c)
        vowels_in_s.sort()
        i = 0
        j = 0
        while j<len(s):
            if s[j] in vowels:
                ans.append(vowels_in_s[i])
                i+=1
            else:
                ans.append(s[j])
            j+=1
        return ''.join(ans)