class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = defaultdict(int)
        for winner, loser in matches:
            if winner not in players:
                players[winner] = 0
            players[loser]+=1
        return [list(sorted([player for player in players if players[player]==0])), list(sorted([player for player in players if players[player]==1]))]