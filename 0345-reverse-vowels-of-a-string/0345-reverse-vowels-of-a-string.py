class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U']
        vlist = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                vlist.append(s[i])
        for i in range(len(s)):
            if s[i] in vowels:
                s[i]=vlist.pop()
        return ''.join(s)
        