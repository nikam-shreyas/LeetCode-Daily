class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderedDict = {letter:counter for counter, letter in enumerate(order)}
        def compare(word):
            return [orderedDict[letter] for letter in word]
        return words == sorted(words, key=compare)