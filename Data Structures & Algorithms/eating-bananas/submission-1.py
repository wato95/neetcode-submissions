class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        l, r = 1, max(piles)

        res = r

        while l <= r:
            k = l + ((r - l) // 2)
            
            rounds = 0
            for pile in piles:
                rounds += math.ceil(float(pile) / k)
                
            if rounds <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
            
            
        return res
            


                
            
