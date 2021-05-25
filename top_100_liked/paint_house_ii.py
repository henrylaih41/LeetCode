import random
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        dp = [[0]*len(costs[0]) for _ in range(2)]
        for i in range(len(costs[0])):
            dp[0][i] = costs[0][i]
        for i in range(1, len(costs)):
            minn = self.getMin(list(dp[(i-1)%2]), 2)
            for j in range(len(costs[0])):
                dp[i%2][j] = minn[0] if dp[(i-1)%2][j] != minn[0] else minn[1]
                dp[i%2][j] += costs[i][j]
        result = math.inf
        for j in range(len(costs[0])):
            result = min(result, dp[(len(costs)-1)%2][j])
        return result
        
    ### O(len(arr) + tlogt) 
    def getMin(self, arr, t):
        return sorted(self.getKthElements(arr, 0, len(arr), t))
        
    def getKthElements(self, arr, l, r, k):
        self.swap(arr, random.randint(l, r-1), r-1)
        pivot = r-1
        j = l
        for i in range(l, r):
            if(arr[i] <= arr[pivot]):
                self.swap(arr, i, j)
                j += 1
        if(j == k):
            return arr[:j]
