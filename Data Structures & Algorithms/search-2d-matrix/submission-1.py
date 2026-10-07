class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix) - 1

        row = -1

        while u <= d:
            mid = u + ((d - u) // 2)
            print(f"mid {mid} {matrix[mid][0]} {matrix[mid][-1]}")
            if (matrix[mid][0] < target) and (matrix[mid][-1] < target):
                u = mid + 1

            elif (matrix[mid][0] > target) and (matrix[mid][-1] > target):
                d = mid - 1

            else:
                row = mid
                break

        print(row)
        if row != -1:
            l, r = 0, len(matrix[0]) - 1

            while l <= r:
                mid = l + ((r - l) // 2)
                print(f"mid {mid}")
                if matrix[row][mid] < target:
                    l = mid + 1

                elif matrix[row][mid] > target:
                    r = mid - 1

                else:
                    return True
        
        return False
        

