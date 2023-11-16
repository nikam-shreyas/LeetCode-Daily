class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def unb(num):
            ans = 0
            power = 0
            for i in range(len(num)-1, -1, -1):
                if num[i]=='1':
                    ans+=pow(2, power)
                power+=1
            return ans
        n = len(nums[0])
        nums = set([n for n in range(0, pow(2, n))]).difference(set([unb(num) for num in nums]))
        def b(num):
            print(num)
            ans = []
            while num>0:
                if num%2==0:
                    ans.append('0')
                else:
                    ans.append('1')
                num//=2
            return ''.join(ans[::-1]).zfill(n)
        return b(nums.pop())
        