class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set()
        words.sort(key = lambda x:len(x))
        output = []
        dp = {}
        def recurse(word, start, curr):
            if (word, start, curr) in dp:
                return dp[(word, start, curr)]
            if curr>=len(word):
                return False
            if curr==len(word)-1 and word[start:curr+1] in wordset:
                dp[(word, start, curr)] = True
                return True
            if word[start:curr+1] in wordset:
                dp[(word, start, curr)] = recurse(word, curr+1, curr+1) or recurse(word, start, curr+1)
                return dp[(word, start, curr)]
            dp[(word, start, curr)] = recurse(word, start, curr+1)
            return dp[(word, start, curr)]
        
        for word in words:
            i=0
            if recurse(word, 0, 0):
                output.append(word)
            wordset.add(word)
        return output
                