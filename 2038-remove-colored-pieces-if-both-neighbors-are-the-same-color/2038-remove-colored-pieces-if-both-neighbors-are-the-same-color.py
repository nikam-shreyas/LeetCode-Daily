class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        As = 0
        Bs = 0
        for i in range(1, len(colors)-1):
            if colors[i]==colors[i-1]==colors[i+1]:
                if colors[i]=='A':
                    As+=1
                else:
                    Bs+=1
        return As>Bs
            
        