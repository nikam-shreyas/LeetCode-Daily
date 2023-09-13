class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1 for i in range(n)]
        right = [1 for i in range(n)]
        for i in range(1, n):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
            if ratings[n-1-i]>ratings[n-i]:
                right[n-1-i]=right[n-i]+1
        candies = 0
        for i in range(n):
            candies+=max(left[i], right[i])
        return candies