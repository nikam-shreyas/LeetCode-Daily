class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        totalBeams = 0
        curr = 0
        for row in bank:
            numBeams = Counter(row)['1']
            totalBeams+=(curr*numBeams)
            if numBeams>0:
                curr=numBeams
        return totalBeams
        