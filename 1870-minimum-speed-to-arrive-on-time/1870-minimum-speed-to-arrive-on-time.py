from math import ceil

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # Get the number of trains
        n = len(dist)

        # Initialize the minimum possible speed to 1
        minSpeed = 1

        # Calculate the total distance of the journey
        totalDistance = sum(dist)

        # Check if there is enough time to catch all the trains
        if hour <= n - 1:
            return -1

        # Calculate the maximum possible speed
        maxSpeed = ceil(totalDistance / (hour - n + 1))

        # Variable to store the final answer
        correctSpeed = -1

        # Binary search loop to find the minimum required speed
        while minSpeed <= maxSpeed:
            # Calculate the middle speed to check
            midSpeed = (minSpeed + maxSpeed) // 2

            # Variable to store the total time required for the commute at midSpeed
            totalTime = 0

            # Calculate the total time required for all trains except the last one
            for i in range(len(dist) - 1):
                totalTime += ceil(dist[i] / midSpeed)

            # Calculate the time required for the last train
            totalTime += dist[-1] / midSpeed

            # Compare totalTime with the given hour
            if totalTime <= hour:
                # If totalTime is within the given hour, update maxSpeed and correctSpeed
                maxSpeed = midSpeed - 1
                correctSpeed = midSpeed
            else:
                # If totalTime exceeds the given hour, update minSpeed
                minSpeed = midSpeed + 1

        # Return the minimum required speed to reach the office on time
        return correctSpeed

# Test cases can be added here to validate the solution
