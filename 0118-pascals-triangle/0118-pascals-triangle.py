class Solution:
    def __init__(self):
        self.ans = [[1]]
    
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<len(self.ans):
            return self.ans[:numRows]
        temp = [0]+self.ans[-1]+[0]
        for i in range(len(self.ans), numRows):
            temp2 = [0]
            for j in range(1, len(temp)):
                temp2.append(temp[j]+temp[j-1])
            temp2.append(0)
            temp = temp2[:]
            self.ans.append(temp2[1:-1])
        return self.ans
            