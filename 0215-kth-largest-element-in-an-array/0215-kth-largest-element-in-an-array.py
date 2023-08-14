class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minValue, maxValue = inf, -inf
        for num in nums:
            if num>maxValue:
                maxValue = num
            if num<minValue:
                minValue = num
        
        count = [0 for _ in range(maxValue-minValue+1)]
        for num in nums:
            count[num-minValue]+=1
        
        for index in range(len(count)-1,-1,-1):
            num = count[index]
            k-=num
            if k<=0:
                return index+minValue
        
        return minValue
            
        