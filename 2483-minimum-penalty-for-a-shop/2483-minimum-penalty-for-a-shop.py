class Solution:
    def bestClosingTime(self, customers: str) -> int:
        leftNs = [0]
        rightYs = [0]
        n = len(customers)
        for i in range(n):
            if customers[i]=='N':
                leftNs.append(leftNs[-1]+1)
            else:
                leftNs.append(leftNs[-1])
            if customers[n-i-1]=='Y':
                rightYs.append(rightYs[-1]+1)
            else:
                rightYs.append(rightYs[-1])
        minI = -1
        minVal = inf
        for i in range(n+1):
            if rightYs[n-i]+leftNs[i]<minVal:
                minVal = rightYs[n-i]+leftNs[i]
                minI = i
        return minI
            