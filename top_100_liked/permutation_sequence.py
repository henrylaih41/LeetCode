class Solution:
    def v1getPermutation(self, n: int, k: int) -> str:
        cnt = 1
        arr = [i for i in range(1, n+1)]
        while(cnt != k):
            self.nextPermutation(arr)
            cnt += 1
        return "".join([str(i) for i in arr])
    
    def getPermutation(self, n, k):
        k -= 1
        result = []
        arr = [i for i in range(1, n+1)]
        divid, d = 1, n-1
        for i in range(2, n):
            divid *= i
        ### divid == (n-1)!
        while(k != 0):
            i = k // divid
            k -= divid * i
            result.append(str(arr[i]))
            arr.pop(i)
            divid //= d
            d -= 1
        for n in arr:
            result.append(str(n))
        return "".join(result)
    
    def nextPermutation(self, nums):
        ### find first decreasing
        di = -1
        for i in range(len(nums)-2, -1, -1):
            if(nums[i] < nums[i+1]):
                di = i
                break
        ### swap di with first element bigger than it from back and reverse di+1 ~ len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if(nums[i] > nums[di]):
                self.swap(nums, i, di)
                j, k = di+1, len(nums)-1
                while(j < k):
                    self.swap(nums, j, k)
                    j += 1
                    k -= 1
                break
        
    def swap(self, nums, i, j):
