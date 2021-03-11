class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) == 0):
            return 0
        maxx, head = 0, prices[0] 
        for i in range(len(prices)):
            head = min(head, prices[i])
            maxx = max(maxx, prices[i] - head)
        return maxx
