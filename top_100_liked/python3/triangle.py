class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] ### cur level 
        for row in triangle:
            n_dp = []
            for i in range(len(row)):
                minn = math.inf
                if(i - 1 >= 0):
                    minn = min(dp[i-1], minn)
                if(i < len(dp)):
                    minn = min(dp[i], minn)
                n_dp.append(row[i] + minn)
            dp = n_dp
        return min(dp)
