# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l, r = 0, n+1

        while l < r:
            m = l + ((r-l)//2)

            res = guess(m)
            print(m, res)
            if res == 0:
                return m
            
            elif res == -1:
                r = m
            
            else:
                l = m + 1
        
        return m