class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        n = len(dist)
        
        minSpeed = 1
        
        totalDistance = sum(dist)
        
        if hour<=n-1:
            return -1
        
        maxSpeed = ceil(totalDistance / (hour-n+1))
        
        possible = False
        
        correctSpeed = -1
        
        while minSpeed<=maxSpeed:
            midSpeed = (minSpeed+maxSpeed)//2
            
            totalTime = 0
            
            for i in range(len(dist)-1):
                totalTime+=ceil(dist[i]/midSpeed)
            
            totalTime += dist[-1] / midSpeed
            
            if totalTime <= hour:
                maxSpeed = midSpeed-1
                correctSpeed = midSpeed
                
            else:
                minSpeed = midSpeed+1
                
        return correctSpeed
            
        
       
            