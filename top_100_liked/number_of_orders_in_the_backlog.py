import heapq 
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        mod = 1e9 + 7
        minh, maxh = [], []
        for order in orders:
            self.operate(minh, maxh, order)
        summ = 0
        for _, nums in minh:
            summ += nums
        for _, nums in maxh:
            summ += nums
        return int(summ % mod)
        
    def operate(self, minh, maxh, order):
        price, amount, typ = order
        # sell
        if(typ):
            while(amount):
                if(len(maxh) and -maxh[0][0] >= price):
                    if(maxh[0][1] > amount):
                        p, n = heappop(maxh)
                        heappush(maxh, (p, n - amount))
                        amount = 0
                    else:
                        _, nums = heappop(maxh)
                        amount -= nums
                else:
                    break
            if(amount):
                heappush(minh, (price, amount))
        # buy
        else:
            while(amount):
                if(len(minh) and price >= minh[0][0]):
                    if(minh[0][1] > amount):
                        p, n = heappop(minh)
                        heappush(minh, (p, n - amount))
                        amount = 0
                    else:
                        _, nums = heappop(minh)
                        amount -= nums
                else:
                    break
            if(amount):
                heappush(maxh, (-price, amount))
        
