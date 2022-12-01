class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        s1 = s[:n//2]
        s2 = s[n//2:]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        c1 = 0
        c2 = 0
        for i in range(n//2):
            if s1[i] in vowels:
                c1+=1
            if s2[i] in vowels:
                c2+=1
        return c1==c2
                