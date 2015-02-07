__author__ = 'Tong'
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one
# and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        profit = 0
        bought = False
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                if bought:
                    pass
                    # print("Day " + i.__str__() + ": Hold")
                else:
                    profit -= prices[i]
                    bought = True
                    # print("Day " + i.__str__() + ": Bought")
            else:
                if bought:
                    profit += prices[i]
                    bought = False
                    # print("Day " + i.__str__() + ": Sold")
                else:
                    pass
                    # print("Day " + i.__str__() + ": Hold")

        if bought:
            # print("Day " + (len(prices) - 1).__str__() + ": Sold")
            return profit + prices[-1]
        else:
            return profit


print(Solution().maxProfit([2, 1]))
print(Solution().maxProfit([1, 3, 2, 22, 212, 56, 12, 8, 21, 4, 5]))