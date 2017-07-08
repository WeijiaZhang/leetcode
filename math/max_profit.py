class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        # brute-force approach: time-limit exceeded
        # dynamic programming: a[i]-a[i-3]=a[i]-a[i-1]+a[i-1]-a[i-2]+a[i-2]-a[i-3]
        dp, profit_max = 0, 0
        # for i in range(1, days):
        #     dp += (prices[i] - prices[i-1])
        #     dp = max(0, dp)
        #     profit_max = max(profit_max, dp)

        price_min = 0
        for i in range(0, days):
            price_min = min(price_min, prices[i])
            profit_max = max(profit_max, (prices[i] - price_min))
        return profit_max
