class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        def bSearch(k):
            low = 0
            high = len(potions)-1
            while low<=high:
                mid = low+(high-low)//2
                if potions[mid]*k>=success:
                    high=mid-1
                else:
                    low=mid+1
            return low
                    
            
        n = len(potions)
        for spell in spells:
            ans.append(n-bSearch(spell))
        return ans