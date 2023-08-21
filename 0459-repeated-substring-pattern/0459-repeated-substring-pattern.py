class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        def check(substr):
            i=0
            j=0
            m = len(substr)
            
            while i<len(s):
                
                if s[i]!=substr[j]:
                    return False
                j=(j+1)%m
                i+=1
            return True
        
        for j in range(1, n):
            if n%j==0:
                if check(s[:j]):
                    return True
        return False