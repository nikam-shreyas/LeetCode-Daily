class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        merge = [(start, 'f', end, None) for start, end in flowers]+[( p, 'p',  p, i) for i, p in enumerate(people)]
        starts = []
        ends = []
        
        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)
            
        starts.sort()
        ends.sort()
        ans = []

        for person in people:
            i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            ans.append(i - j)
        
        return ans
                