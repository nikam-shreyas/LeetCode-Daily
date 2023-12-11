from bisect import bisect_left, bisect_right
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [-1]
        
        for index, char in enumerate(s):
            if char=='|':
                candles.append(index)
        
        candles.append(candles[-1]+1)
        print(candles)
        if len(candles)==2:
            return [0 * len(queries)]
        ans = []
        for start, end in queries:
            left = bisect_left(candles, start)
            right = bisect_right(candles, end)-1
            print(left, right)
            if left>=right:
                ans.append(0)
            else:
                total_candles = (candles[right]-candles[left]) - (right-left)
                ans.append(total_candles)
        return ans