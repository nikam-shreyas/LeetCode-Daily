class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        counter = defaultdict(int)
        for word in words:
            for char in word:
                counter[char]+=1
        for char in counter:
            if counter[char]%n!=0:
                return False
        return True