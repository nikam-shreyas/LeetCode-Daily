from heapq import heapify, heappop

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        bag = [(-value, label) for value, label in zip(values, labels)]
        heapify(bag)
        chosenSet = defaultdict(int)
        score = 0
        count = 0
        while bag:
            value, label = heappop(bag)
            if chosenSet[label]<useLimit:
                chosenSet[label]+=1
                score-=value
                count+=1
            if count==numWanted:
                break
        return score
            