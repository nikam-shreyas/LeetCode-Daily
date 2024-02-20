class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return Counter(bin(n))['1']==1 and n>0