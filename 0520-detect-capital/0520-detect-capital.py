class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def cond1(word):
            return all([ord('A')<=ord(x)<=ord('Z') for x in word])
            #     return True
            # return False
        def cond2(word):
            return all([ord('a')<=ord(x)<=ord('z') for x in word])
            #     return True
            # return False
        def cond3(word):
            return ord('A')<=ord(word[0])<=ord('Z') and cond2(word[1:])
            #     return True
            # return False
        word = [x for x in word]
        return cond1(word) or cond2(word) or cond3(word)
        # def cond(word):
        #     return word[0]==word[0].upper() and word[1:]==word[1:].lower()
        # return word==word.lower() or word==word.upper() or cond(word)
            