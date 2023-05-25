class Solution:
    def longestDecomposition(self, text: str) -> int:
        end = len(text)
        count = 0
        i=0
        j=end-1
        while i<=j:
            while i<j and text[i]!=text[j]:
                j-=1
            newlen = end-j
            flag = True
            for k in range(newlen):
                if text[i+k]!=text[j+k]:
                    flag=False
                    break
            if flag:
                if i==j:
                    count+=1
                else:
                    count+=2
                end=j
                j-=1
                i+=newlen
            else:
                j-=1
        
        return count
            
            