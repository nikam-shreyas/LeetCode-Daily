class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Define a recursive function to search for the target in a given submatrix
        def recurse(lowr, highr, lowc, highc):
            # Base case: check if the current submatrix is valid
            if lowr <= highr and lowc <= highc:
                # Calculate mid row and mid column
                midr = lowr + (highr - lowr) // 2
                midc = lowc + (highc - lowc) // 2
                
                # Check if midr and midc are within matrix boundaries
                if not (0 <= midr < m and 0 <= midc < n):
                    return False
                
                # Check if the target is found at the middle element
                if matrix[midr][midc] == target:
                    return True
                # If target is greater, search in the bottom-right and top-right submatrices
                elif matrix[midr][midc] < target:
                    return recurse(midr + 1, highr, lowc, highc) or recurse(lowr, highr, midc + 1, highc)
                # If target is smaller, search in the top-left and bottom-left submatrices
                else:
                    return recurse(lowr, midr - 1, lowc, highc) or recurse(lowr, highr, lowc, midc - 1)
            return False
        
        # Get the number of rows and columns in the matrix
        m = len(matrix)
        n = len(matrix[0])
        
        # Start the recursive search from the entire matrix
        return recurse(0, m, 0, n)
