from heapq import heapify, heappush, heappop
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        h = [(index, num, 0) for index, num in enumerate(arr)]
        l = len(arr)
        if k>l:
            return max(arr)
        heapify(h)
        while True:
            index1, num1, count1 = heappop(h)
            index2, num2, count2 = heappop(h)
            if num1>num2:
                count1+=1
                if count1==k:
                    return num1
                heappush(h, (0, num1, count1))
                heappush(h, (l+1, num2, count2))
                l+=1
            else:
                count2+=1
                if count2==k:
                    return num2
                heappush(h, (0, num2, count2))
                heappush(h, (l+1, num1, count1))
                l+=1
        
                
        
        