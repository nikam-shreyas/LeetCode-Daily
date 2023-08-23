from heapq import heapify, heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxval = max(counter.values())
        rem = len(s)-maxval
        if rem<maxval-1:
            return ""
        h = [(-val, key) for key, val in counter.items()]
        heapify(h)
        # print(h)
        ans = ['']
        while h:
            # print(h, ans)
            val, currs = heappop(h)
            if currs==ans[-1]:
                if h:
                    val2, currs2 = heappop(h)
                    val2+=1
                    ans.append(currs2)
                    if val2!=0:
                        heappush(h, (val2, currs2))
                else:
                    return ""
                heappush(h, (val, currs))
            else:
                ans.append(currs)
                val+=1
                if val!=0:
                    heappush(h, (val, currs))
        return ''.join(ans)
                
                    
                
        