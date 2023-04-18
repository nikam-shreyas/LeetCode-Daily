class Solution:
    def addMinimum(self, word: str) -> int:
        word2 ='abc'
        i=0
        j=0
        count=0
        while i<len(word):
            if word[i]==word2[j%3]:
                i+=1
                j+=1
            else:
                j+=1
                count+=1
        while j%3!=0:
            count+=1
            j+=1
        return count