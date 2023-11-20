from collections import Counter
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        houses = len(garbage)
        garbage = [Counter(g) for g in garbage]
        total_time = 0
        def truck(g_type):
            time = garbage[0][g_type]
            time_to_get_here = 0
            for i in range(1, houses):
                time_to_get_here += travel[i-1]
                if g_type in garbage[i]:
                    time+=garbage[i][g_type]
                    time+=time_to_get_here
                    time_to_get_here=0
            return time
        return truck('M')+truck('G')+truck('P')