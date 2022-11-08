class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        prev_string = None
        d = {}
        for i in range(ord('a'), ord('z')+1):
            d[chr(i)]=chr(ord('A')+i-ord('a'))
            d[chr(ord('A')+i-ord('a'))]=chr(i)
        while prev_string!=s:
            prev_string=s[:]
            i=0
            while 0<=i<len(s)-1:
                print(i, len(s), s)
                if s[i]==d[s[i+1]]:
                    del s[i]
                    del s[i]
                    i-=1
                i+=1
        return ''.join(s)

