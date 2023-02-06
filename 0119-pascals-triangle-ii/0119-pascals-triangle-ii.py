class Solution:
    def __init__(self):
        self.triangle = [[1]]
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex<len(self.triangle):
            return self.triangle[rowIndex]
        i = len(self.triangle)
        temp = [0]+self.triangle[-1]+[0]
        while i<=rowIndex:
            temp2 = [0]
            for j in range(1, len(temp)):
                temp2.append(temp[j]+temp[j-1])
            temp2.append(0)
            temp = temp2
            self.triangle.append(temp[1:-1])
            i+=1
        return self.triangle[rowIndex]