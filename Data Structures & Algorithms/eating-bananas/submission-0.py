import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_rate = max(piles)
        min_rate = 1

        while min_rate <= max_rate:
            time = 0
            mid_rate = min_rate + ((max_rate - min_rate)//2)
            print(f"{min_rate} {mid_rate} {max_rate}")
            
            for i in piles:
                time += math.ceil(i/mid_rate)
            
            print(f"time {time} for rate {mid_rate}")
            
            if time > h:
                min_rate = mid_rate + 1

            elif time <= h:
                max_rate = mid_rate - 1
            print(f"{min_rate} {mid_rate} {max_rate}")
            
        return min_rate

        