class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1


        while l < r:
            m = l + ((r - l) // 2)

            if matrix[m][0] <= target:
                if matrix[m][len(matrix[m])-1] < target:
                    l = m + 1
                else:
                    l = m
                    break
            
            else:
                r = m - 1
        
        print(l, r)

        i, j = 0, len(matrix[l]) - 1

        while i <= j:
            n = i + ((j - i) // 2)

            if matrix[l][n] < target:
                i = n + 1
            
            elif matrix[l][n] > target:
                j = n - 1
            
            else:
                return True
        
        return False



        