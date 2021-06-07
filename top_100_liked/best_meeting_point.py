import random
class Solution:        
    def v1minTotalDistance(self, grid: List[List[int]]) -> int:
        x, y = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    x.append(i)
                    y.append(j)
        median_x = self.findKth(x, 0, len(x)-1, len(x)//2)
        median_y = self.findKth(y, 0, len(y)-1, len(y)//2)
        summ = 0
        for n in x:
            summ += abs(n-median_x)
        for n in y:
            summ += abs(n-median_y)
        return summ
    
    def findKth(self, arr, lo, hi, target):
        self.swap(arr, random.randint(lo, hi), hi)
        j = lo
        for i in range(lo, hi+1):
            if(arr[i] <= arr[hi]):
                self.swap(arr, i, j)
                j += 1
        j -= 1
        if(j == target):
            return arr[j]
