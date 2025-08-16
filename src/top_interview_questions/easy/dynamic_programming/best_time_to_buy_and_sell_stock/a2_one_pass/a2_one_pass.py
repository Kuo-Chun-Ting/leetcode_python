class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for i, _ in enumerate(prices):
            if prices[i] < min_price:
                min_price = prices[i]
                continue
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                continue

        return int(max_profit)
