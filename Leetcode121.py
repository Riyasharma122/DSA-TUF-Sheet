class Solution:
    def maxprofit(self,prices):
        min_price = prices[0]
        max_profit =0
        for i in range(1,len(prices)):
            profit= prices[i]-min_price
            max_profit = max(profit,max_profit)
            min_price = min(prices[i],min_price)
        return max_profit