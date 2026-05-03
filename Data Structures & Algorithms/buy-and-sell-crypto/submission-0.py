class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        i = 0
        j = 1

        while j < len(prices):
            if prices[j] - prices[i] < 0:
                i = j
                j += 1
            else:
                maxProfit = max(maxProfit, prices[j] - prices[i])
                j += 1
        
        return maxProfit
