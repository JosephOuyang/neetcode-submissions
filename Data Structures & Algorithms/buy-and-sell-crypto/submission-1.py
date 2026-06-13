class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer solution
        maxDiff = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                currDiff = prices[right] - prices[left]
                if currDiff > maxDiff:
                    maxDiff = currDiff
                right += 1
        return maxDiff
        