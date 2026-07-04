# Problem: Best Time to Buy and Sell Stock
# LeetCode: 121
# Difficulty: Easy
# Topic: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]

        :rtype: int
        """
        min_price=prices[0]
        max_profit=0
        for price in prices:
            if price<=min_price:
                min_price=price
            profit=price-min_price
            max_profit=max(max_profit,profit)
        return max_profit
        