class Solution:
    def countHomogenous(self, s: str) -> int:
        modu = pow(10, 9)+7
        def get_combi(n):
            return (n*(n+1))//2
        total_count = 0
        i = 0
        j = 0
        while j<len(s):
            if s[i]==s[j]:
                j+=1
            else:
                total_count+=get_combi(j-i)%modu
                i = j
        total_count+=get_combi(j-i)%modu
        return total_count
                