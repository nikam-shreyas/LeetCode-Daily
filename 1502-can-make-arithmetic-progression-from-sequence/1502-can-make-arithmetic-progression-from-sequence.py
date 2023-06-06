class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        a = arr[0]
        d = arr[1]-arr[0]
        for index, num in enumerate(arr):
            # print(index)
            if num!=a+(index*d):
                return False
        return True
            