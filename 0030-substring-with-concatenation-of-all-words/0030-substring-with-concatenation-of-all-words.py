class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordset = set(words)
        wordscount = len(words)
        wordlen = len(words[0])
        ans = []
        def check(i):
            temp = words[:]
            k = i
            while temp:
                if s[k:k+wordlen] in temp:
                    temp.remove(s[k:k+wordlen])
                    k+=wordlen
                else:
                    return False
            return temp==[]
        for i in range(len(s)-(wordlen*wordscount)+1):
            if s[i:i+wordlen] in wordset:
                if check(i):
                    ans.append(i)
        return ans