from bisect import bisect_right
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        temp = bisect_right(letters, target)
        if temp>=len(letters):
            return letters[0]        
        return letters[temp]