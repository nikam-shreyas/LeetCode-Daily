from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        counter1 = Counter(s1)
        for i in range(len(s2)-n+1):
            window = s2[i:i+n]
            counter2 = Counter(window)
            if counter1==counter2:
                return True
        return False