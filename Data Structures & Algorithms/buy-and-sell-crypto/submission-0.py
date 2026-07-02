class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        r = 0
        profit = 0
        sell = [0]*n
        for i in range(n-1,-1,-1):
            sell[i] = r
            r = max(prices[i],r)

        for i in range(n):
            pro = sell[i] - prices[i]
            profit = max(pro,profit)
    
        return profit

        