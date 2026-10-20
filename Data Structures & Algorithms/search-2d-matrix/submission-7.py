class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1


        while l <= r:
            m = l + ((r - l) // 2)

            if matrix[m][-1] < target:
                l = m + 1
            
            elif matrix[m][0] > target:
                r = m - 1
            
            else:
                break

        if l > r:
            return False

        i, j = 0, len(matrix[m]) - 1

        while i <= j:
            n = i + ((j - i) // 2)

            if matrix[m][n] < target:
                i = n + 1
            
            elif matrix[m][n] > target:
                j = n - 1
            
            else:
                return True
        
        return False



        