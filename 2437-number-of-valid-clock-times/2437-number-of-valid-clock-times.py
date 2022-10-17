class Solution:
    def countTime(self, time: str) -> int:
        time = list(''.join(time.split(':')))
        count = 0
        ans = []
        skiphr = False
        if time[0]=='?':
            if time[1]=='?':
                ans.append(24)
                skiphr = True
            elif int(time[1])<=3:
                ans.append(3)
            else:
                ans.append(2)
        if not skiphr:
            if time[1]=='?':
                if int(time[0])<2:
                    ans.append(10)
                else:
                    ans.append(4)
        skipmin = False
        if time[2]=='?':
            if time[3]=='?':
                skipmin=True
                ans.append(60)
            else:
                ans.append(6)
        if not skipmin:
            if time[3]=='?':
                ans.append(10)
        
        if not ans:
            return 1
        count = 1
        for i in ans:
            count*=i
        return count