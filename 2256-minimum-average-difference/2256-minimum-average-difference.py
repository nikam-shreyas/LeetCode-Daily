class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        leftsum = [0]*n
        leftsum[0]=nums[0]
        rightsum = [0]*n
        for i in range(1, n):
            leftsum[i]=nums[i]+leftsum[i-1]
            rightsum[n-1-i]=nums[n-i]+rightsum[n-i]
        minsum = inf
        minidx = -1
        for i in range(n):
            if n-i-1!=0:
                temp = abs((leftsum[i]//(i+1))-(rightsum[i]//(n-i-1)))
            else:
                temp=abs((leftsum[i]//(i+1))-0)
            if temp<minsum:
                minsum=temp
                minidx = i
        return minidx
        
        