class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def recurse(lowr, highr, lowc, highc):
            if lowr<=highr and lowc<=highc:
                midr = lowr+(highr-lowr)//2
                midc = lowc+(highc-lowc)//2
                if not(0<=midr<m and 0<=midc<n):
                    return False
                if matrix[midr][midc]==target:
                    return True
                elif matrix[midr][midc]<target:
                    return recurse(midr+1, highr, lowc, highc) or recurse(lowr, highr, midc+1, highc)
                else:
                    return recurse(lowr, midr-1, lowc, highc) or recurse(lowr, highr, lowc, midc-1)
            return False
        m = len(matrix)
        n = len(matrix[0])
        return recurse(0, m, 0, n)