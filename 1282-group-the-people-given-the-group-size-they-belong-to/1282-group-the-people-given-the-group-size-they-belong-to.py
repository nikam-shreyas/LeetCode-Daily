from collections import Counter
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        gs = Counter(groupSizes)
        for key, val in gs.items():
            temp = val//key
            gs[key] = [[] for _ in range(temp)]
        its = {i:0 for i in gs.keys()}
        for person in range(len(groupSizes)):
            group = groupSizes[person]
            if len(gs[group][its[group]])==group:
                its[group]+=1
            gs[group][its[group]].append(person)
        ans = []
        for _, val in gs.items():
            ans.extend(val)
        return ans
        
            
        