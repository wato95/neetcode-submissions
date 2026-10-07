class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r - l)//2)

            mm = m * m
            if mm > x:
                r = m - 1
            
            elif mm == x:
                return m

            else:
                l = m + 1
                res = m
            
        return res