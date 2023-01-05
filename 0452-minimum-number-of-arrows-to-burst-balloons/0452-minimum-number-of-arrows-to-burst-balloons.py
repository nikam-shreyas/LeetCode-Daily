class Solution:
    def findMinArrowShots(self, s: List[List[int]]) -> int:
        s.sort(key = lambda i: i[1])
        k = 1
        aim = s.pop(0)[1]
        for i in s:
            if i[0] > aim:
                aim = i[1]
                k += 1
        return k