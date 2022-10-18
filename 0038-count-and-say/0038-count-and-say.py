class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        def recurse(num):
            i = 0
            ans  = ""
            while i<len(num):
                count=1
                while i+1<len(num) and num[i]==num[i+1]:
                    i+=1
                    count+=1
                i+=1
                ans+=str(count)+num[i-1]
            return ans
        for i in range(n-1):
            ans = recurse(ans)
        return ans
                