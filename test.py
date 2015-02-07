class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        p = 0
        for i in range(len(prices)-1):
            p += max(prices[i+1] - prices[i], 0)
        return p

print(Solution().maxProfit([1, 3, 2,22, 212, 56, 12, 8, 21, 4, 5]))