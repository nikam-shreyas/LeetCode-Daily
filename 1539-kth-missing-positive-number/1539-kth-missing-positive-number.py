class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        index = 1
        j = 0
        while j<len(arr) and k>0:
            if index==arr[j]:
                index+=1
                j+=1
            else:
                index+=1
                k-=1
        while k>0:
            index+=1
            k-=1
        return index-1