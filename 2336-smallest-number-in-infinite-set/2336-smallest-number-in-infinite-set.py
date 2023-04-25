from heapq import heapify, heappush, heappop, nlargest
class SmallestInfiniteSet:

    def __init__(self):
        self.a = [1, 2, 3, 4, 5]
        heapify(self.a)

    def popSmallest(self) -> int:
        # print(self.a)
        temp = heappop(self.a)
        heappush(self.a, nlargest(1,self.a)[0]+1)
        # print(self.a)
        # print()
        return temp
        

    def addBack(self, num: int) -> None:
        if num>self.a[-1]:
            return
        if num in self.a:
            return
        heappush(self.a, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)