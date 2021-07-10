class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ### make prices unique
        np = [prices[0]]
        for i in range(1, len(prices)):
            if(prices[i] != np[-1]):
                np.append(prices[i])
        prices = np
        ### edge
        if(len(prices) == 1):
            return 0
        peak, profits = [prices[0]], 0
        ### find all peaks (unique peak)
        for i in range(1, len(prices)-1):
            if((prices[i] - prices[i-1]) * (prices[i] - prices[i+1]) > 0):
                peak.append(prices[i])
        peak.append(prices[-1])
        i = 0
        if(peak[0] > peak[1]):
            i = 1
        while(i+1 < len(peak)):
            profits += (peak[i+1] - peak[i])
            i += 2
        return profits
