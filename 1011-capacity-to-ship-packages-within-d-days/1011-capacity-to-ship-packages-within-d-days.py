class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # divide the weights in contiguous d parts such that the max sum is minimized
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left + right) // 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D: left = mid + 1
            else: right = mid
        return left