class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        
        l = 0
        r = n - 1

        while l < r:
            l_height = heights[l]
            r_height = heights[r]

            area = (r - l) * min(l_height, r_height)

            max_area = max(area, max_area)

            if l_height <= r_height:
                l += 1
            else:
                r -= 1
        
        return max_area
            

            