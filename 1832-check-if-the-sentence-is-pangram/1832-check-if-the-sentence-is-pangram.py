class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chars = [False for i in range(26)]
        for char_ in sentence.lower():
            chars[ord(char_)-ord('a')]=True
        return all(chars)