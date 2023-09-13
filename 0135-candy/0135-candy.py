class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Number of children
        num_children = len(ratings)

        # Initialize left and right candy counts to 1 for each child
        left_candy = [1] * num_children  
        right_candy = [1] * num_children

        # Iterate through ratings from left to right
        for i in range(1, num_children):
          # If current rating is greater than previous, 
          # increment left candy count
            if ratings[i] > ratings[i-1]:
                left_candy[i] = left_candy[i-1] + 1

          # If current rating is greater than previous,
          # increment right candy count 
            if ratings[num_children-i-1] > ratings[num_children-i]:
                right_candy[num_children-i-1] = right_candy[num_children-i] + 1

        # Initialize variable to track total candies needed  
        total_candies = 0

        # Take maximum of left and right candy counts for each child
        for i in range(num_children):
            total_candies += max(left_candy[i], right_candy[i])

        return total_candies