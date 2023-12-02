class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        s = 0
        for word in words:
            word_counter = Counter(word)
            flag = True
            for k in word_counter:
                if k not in chars_counter or word_counter[k]>chars_counter[k]:
                    flag = False
                    break
            if flag:
                s+=len(word)
        return s