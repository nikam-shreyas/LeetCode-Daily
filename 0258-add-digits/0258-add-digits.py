class Solution:
    def addDigits(self, num: int) -> int:
        nums = [0, num]        
        while len(nums)>1:
            num = sum(nums)  
            nums = []
            while num>0:
                nums.append(num%10)
                num = num//10
        return nums[0] if nums else 0