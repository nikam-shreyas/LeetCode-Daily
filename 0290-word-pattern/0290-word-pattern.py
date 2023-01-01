class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_s = {}
        s_pattern = {}
        s = s.split(' ')
        if len(pattern)!=len(s):
            return False
        for i in range(len(pattern)):
            # print(s_pattern, pattern_s)
            character = pattern[i]
            word = s[i]
            if character in pattern_s and word in s_pattern and pattern_s[character]==word and s_pattern[word]==character:
                continue
            elif character not in pattern_s and word not in s_pattern:
                pattern_s[character] = word
                s_pattern[word] = character
            else:
                return False
        return True
            
                
        