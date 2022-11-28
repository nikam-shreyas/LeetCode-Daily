class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost0 = set()
        lost1 = set()
        lost2 = set()
        for _, loser in matches:
            if loser not in lost1 and loser not in lost2:
                lost1.add(loser)
            elif loser in lost1:
                lost1.remove(loser)
                lost2.add(loser)
        for winner, _ in matches:
            if winner not in lost1 and winner not in lost2:
                lost0.add(winner)
        return [sorted(list(lost0)), sorted(list(lost1))]