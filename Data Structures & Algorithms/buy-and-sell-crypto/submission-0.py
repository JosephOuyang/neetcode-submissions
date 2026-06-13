class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force, my first intuition
        maxDiff = 0
        for i in range(len(prices) - 1):
            j = i + 1
            for j in range(j, len(prices)):
                currDiff = prices[j] - prices[i]
                if currDiff > maxDiff:
                    maxDiff = currDiff
        return maxDiff

        