class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        res = 0
        for i in range(1,len(prices)):
            if prices[i] < m:m=prices[i]
            if prices[i] - m > res:res = prices[i] - m
        return res if res > 0 else 0
