class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(num):
            if num=='':
                return False
            if 0<=int(num)<=255:
                if len(num)==1:
                    return True
                if len(num)>1 and num[0]!='0':
                    return True
            return False
        n = len(s)
        ans = []
        for i in range(1, min(4, n)):
            # print(1, s[:i])
            if isValid(s[:i]):
                for j in range(1, min(n-i, 4)):
                    # print(2, s[i:i+j])
                    if isValid(s[i:i+j]):
                        for k in range(1, min(n-j, 4)):
                            # print(3, s[i+j:i+j+k], s[i+j+k:])
                            if isValid(s[i+j:i+j+k]) and isValid(s[i+j+k:]):
                                ans.append(s[:i]+'.'+s[i:i+j]+'.'+s[i+j:i+j+k]+'.'+s[i+j+k:])
        return ans