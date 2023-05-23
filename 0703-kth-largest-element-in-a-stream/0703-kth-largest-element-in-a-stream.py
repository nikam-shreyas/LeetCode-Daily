class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.st = sorted(nums, reverse=True)[:k]
        self.k=k

    def add(self, val: int) -> int:
        temp = []
        while self.st and self.st[-1]<val:
            temp.append(self.st.pop())
        self.st.append(val)
        while len(self.st)<self.k:
            self.st.append(temp.pop())
        self.st = self.st[:self.k]
        return self.st[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)