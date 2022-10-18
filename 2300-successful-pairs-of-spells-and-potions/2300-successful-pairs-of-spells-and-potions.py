class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # # sort the potions
        # # iterate over the spells and find the minimum whose product is >= success
        # # return m-index of the minimum
        # # append this to pairs
        # potions.sort()
        # def binarysearch(target):
        #     l=0
        #     h=len(potions)-1
        #     while l<h:
        #         mid = l+(h-l)//2
        #         if potions[mid]*target>=success:
        #             h=mid-1
        #         else:
        #             l=mid+1
        #     return l
        # pairs = []
        # n = len(spells)
        # m = len(potions)
        # for i in range(n):
        #     index = binarysearch(spells[i])
        #     print(spells[i], index)
        #     if index+1>=n or potions[index+1]*spells[i]<success:
        #         pairs.append(0)
        #     else:
        #         pairs.append(m-index)
        # return pairs
        
        potions.sort()
        return [len(potions) - bisect_left(potions, (success + a - 1) // a) for a in spells]