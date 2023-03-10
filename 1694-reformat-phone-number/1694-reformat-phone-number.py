class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '').replace(' ', '')
        n = len(number)
        i=0
        ans=[]
        while n-i>4:
            ans.append(number[i:i+3])
            i+=3
        if n-i==4:
            ans.append(number[i:i+2])
            ans.append(number[i+2:])
        else:
            ans.append(number[i:])
        return '-'.join(ans)