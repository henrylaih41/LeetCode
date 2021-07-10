class Solution:
    def numSquares(self, n):
        sq_nums = []
        i = 1
        while(i*i <= n):
            sq_nums.append(i*i)
            i += 1
        queue = set([n])
        level = 0
        while(1):
            next_queue = set()
            level += 1
            for nums in queue:
                if(nums in sq_nums):
                    return level
                for sq in sq_nums:
                    if(nums <= sq):
                        break
                    next_queue.add(nums - sq) # == won't occur, so 0 would not appear
            queue = next_queue
            
    def dpnumSquares(self, n: int) -> int:
        self.dp = [math.inf] * (n+1)
        self.dp[0] = 0
        return self.bottom_recur(n)
    
    def top_recur(self, n):
        if(self.dp[n] != math.inf):
            return self.dp[n]
        i = 1
        while(n - i*i >= 0):
            self.dp[n] = min(self.dp[n], self.recur(n - i*i) + 1)
            i += 1
            
        return self.dp[n]
        
    def bottom_recur(self, n):
        for i in range(1, n+1):
            j = 1
            while(i - j*j >= 0):
                self.dp[i] = min(self.dp[i], self.dp[i-j*j] + 1)
                j += 1
        return self.dp[n]
