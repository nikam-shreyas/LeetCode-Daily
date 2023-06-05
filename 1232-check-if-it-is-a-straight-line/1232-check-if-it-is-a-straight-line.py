class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1 = coordinates[0]
        x2,y2 = coordinates[1]
        if x1-x2!=0:
            m=(y1-y2)/(x1-x2)
            c = y1-m*x1
            for x, y in coordinates:
                if y-m*x-c!=0:
                    return False
            return True
        else:
            m=inf
            c=0
            x1 = coordinates[0][0]
            for x, y in coordinates:
                if x!=x1:
                    return False
            return True
        