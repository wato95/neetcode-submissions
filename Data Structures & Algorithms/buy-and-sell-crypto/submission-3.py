class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low = prices[0]
        ans = 0

        for price in prices:
            ans = max(ans, price-low)
            if price < low:
                low = price
                
            
        return ans

