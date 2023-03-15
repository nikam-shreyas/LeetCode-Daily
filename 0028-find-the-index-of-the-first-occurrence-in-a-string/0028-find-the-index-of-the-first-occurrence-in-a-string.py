class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def cal_lps(needle):
            lps = [0 for _ in range(len(needle))]
            i1, j1 = 1,0
            while i1<len(needle):
                if needle[j1] == needle[i1]:
                    j1+=1
                    lps[i1] = j1 
                    i1+=1
                elif needle[j1] != needle[i1] and j1>0:
                    j1 = lps[j1-1]
                elif needle[j1] != needle[i1] and j1==0:
                    lps[i1] = 0
                    i1+=1
            return lps
        
        m = len(haystack)
        n = len(needle)

        i,j = 0,0
        if m<n:
            return -1
        lps = cal_lps(needle)
        # print(lps)
        while i<m:
            # print(i, j)
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                if j==n:
                    return i-n
            elif haystack[i] != needle[j] and j>0:
                j = lps[j-1]
            elif haystack[i] != needle[j] and j==0:
                i+=1
        return -1