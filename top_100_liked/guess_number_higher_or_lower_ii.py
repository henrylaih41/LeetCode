class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        ### init
        for i in range(1, n):
            dp[i][i] = 0
        
        for i in range(n, 0, -1):
            for j in range(i+1, n+1):
                minn = math.inf
                for k in range(i, j+1):
                    if(k == i):
                        minn = min(minn, k + dp[k+1][j])
                    elif(k == j):
                        minn = min(minn, k + dp[i][k-1])
                    else:
                        minn = min(minn, k + max(dp[i][k-1],dp[k+1][j]))
                dp[i][j] = minn
​
        return dp[1][n]
