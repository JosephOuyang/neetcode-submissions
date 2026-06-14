class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                currProfit = prices[sell] - prices[buy]
                if currProfit > maxProfit:
                    maxProfit = currProfit
                sell += 1
        return maxProfit

        