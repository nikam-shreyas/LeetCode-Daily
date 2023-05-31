class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.tuples = defaultdict(list)
        

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checkins[id] = (t, startStation)
        

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        checkinTime, startStation = self.checkins[id]
        del self.checkins[id]
        self.tuples[(startStation, endStation)].append(t-checkinTime)
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        def avg(l):
            return sum(l)/len(l)
        
        return avg(self.tuples[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)