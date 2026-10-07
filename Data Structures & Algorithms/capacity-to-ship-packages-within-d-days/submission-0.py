class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total, maximum = sum(weights), max(weights)

        l = maximum
        r = total

        while l <= r:
            m = l + ((r-l)//2)

            ships = 1
            weight = m
            print(m)

            for i in weights:
                if weight - i >= 0:
                    weight -= i
                else:
                    ships += 1
                    weight = m - i
            
            print(ships)
            if ships > days:
                l = m + 1
            
            else:
                res = m
                r = m - 1
        
        return res
