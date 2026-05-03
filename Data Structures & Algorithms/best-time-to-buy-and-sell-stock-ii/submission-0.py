class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currProfit = 0

        i = 0
        j = 1

        while j < len(prices):
            if prices[j] - prices[i] < 0:
                i += 1
                j += 1
            else:
                currProfit = prices[j] - prices[i]
                maxProfit += currProfit
                i += 1
                j += 1
        return maxProfit 