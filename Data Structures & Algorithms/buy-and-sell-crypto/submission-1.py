class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0
        for p in prices:
            profit = p - min_price
            best = max(best, profit)
            min_price = min(min_price, p)
        return best

        