class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0]*(len(prices))
        sell = [0]*(len(prices))
        buy[0] = prices[0]
        sell[-1] = prices[-1]
        for i in range(1,len(prices)):
            buy[i] = min(prices[i],buy[i-1])
        
        for j in range(len(prices)-2,-1,-1):
            sell[j] = max(prices[j],sell[j+1])
        
        profit = 0
        for k in range(len(prices)):
            diff = sell[k]-buy[k]
            profit = max(diff,profit)

        return profit
        