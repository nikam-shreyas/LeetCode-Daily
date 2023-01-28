class SummaryRanges:

    def __init__(self):
        self.stream = []

    def addNum(self, value: int) -> None:
        self.stream.append([value, value])

    def getIntervals(self) -> List[List[int]]:
        self.stream.sort()
        ans = [self.stream[0]]
        for i in range(1, len(self.stream)):
            # print(ans)
            curr = ans.pop()
            # print(curr, self.stream[i])
            if self.stream[i][0]<=curr[1]+1:
                curr[1] = max(curr[1], self.stream[i][1])
                ans.append(curr)
            else:
                ans.append(curr)
                ans.append(self.stream[i])
        self.stream = ans
        # print(self.stream)
        # print()
        return self.stream


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()