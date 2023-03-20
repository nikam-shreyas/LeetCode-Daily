
class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        count = 0
        if f[0]==0:
            if len(f)>1:
                if f[1]==0:
                    f[0]=1
                    count+=1
            else:
                count+=1
                f[0]=1
        for i in range(1, len(f)-1):
            if f[i]==0 and f[i-1]==0 and f[i+1]==0:
                f[i]=1
                count+=1
        
        if f[-1]==0:
            if len(f)>1:
                if f[-2]==0:
                    f[-1]=1
                    count+=1
            else:
                count+=1
                f[-1]=1
        return count>=n
                
                