class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destinations = set()
        sources = set()
        for start, end in paths:
            destinations.add(end)
            sources.add(start)
            if start in destinations:
                destinations.remove(start)
        for k in destinations:
            if k not in sources:
                return k
        
            