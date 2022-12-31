class Solution:
    def closetTarget(self, words: List[str], target: str, startindex: int) -> int:
        # target not in words: return -1
        n = len(words)
        if target not in words:
            return -1
        # count = 1
        count = 0
        # from start_index go back and front till you encounter target
        # iterate using while
        while True:
            front = (startindex + count)%n
            back = (startindex - count + n)%n
        # if you encounter target, then return count
            if words[front]==target or words[back]==target:
                return count
            count+=1
        
        