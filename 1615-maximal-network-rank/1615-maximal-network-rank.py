from collections import defaultdict

class Solution:

    def maximalNetworkRank(self, numCities: int, roads: List[List[int]]) -> int:

        # Create an adjacency list to represent connections between cities
        adjList = defaultdict(set) 

        for startCity, endCity in roads:

            # Add road connections in both directions
            adjList[startCity].add((startCity, endCity))  
            adjList[endCity].add((startCity, endCity))

        maxRank = 0

        # Loop through all pairs of cities to find max connections
        for city1 in range(numCities-1):
            
            for city2 in range(city1+1, numCities):

                # Get all combined road connections between two cities
                connections = adjList[city1].union(adjList[city2])

                rank = len(connections)

                # Update max rank
                maxRank = max(maxRank, rank)

        return maxRank