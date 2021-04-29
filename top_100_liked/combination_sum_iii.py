class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [i for i in range(1, 10)]
        return self.solve(n, 0, arr, k)
    
    def solve(self, remain, i, arr, k):
        if(remain == 0 and k == 0):
            return [tuple()]
        if(remain < 0 or k <= 0 or i >= len(arr)):
            return []
        result = []
        ### take i 
        for l in self.solve(remain - arr[i], i+1, arr, k-1):
            result.append((arr[i], ) + l)
        ### don't take i
        for l in self.solve(remain, i+1, arr, k):
            result.append(l)
        return result
