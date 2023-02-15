class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        array_k = []
        while k>0:
            array_k.append(k%10)
            k=k//10
        num = num[::-1]
        # array_k=array_k[::-1]
        ans = []
        i = 0
        j = 0
        s=0
        c=0
        while i<len(num) and j<len(array_k):
            s=num[i]+array_k[j]+c
            if s>=10:
                c=1
                s=s%10
            else:
                c=0
            ans.append(s)
            i+=1
            j+=1
        while i<len(num):
            s=num[i]+c
            if s>=10:
                c=1
                s=s%10
            else:
                c=0
            ans.append(s)
            i+=1
        while j<len(array_k):
            s=array_k[j]+c
            if s>=10:
                c=1
                s=s%10
            else:
                c=0
            ans.append(s)
            j+=1
        if c>0:
            ans.append(1)
        return ans[::-1]
            
         
        