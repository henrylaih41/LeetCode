class Solution:
    ### radix sort O(d(n+b)) d = logb(max in nums)
    def maximumGap(self, nums: List[int]) -> int:
        if(len(nums) <= 1):
            return 0
        maxx = int(1e9)
        divider = 1
        while(divider <= maxx):
            self.countSort(nums, divider)
            divider *= 10
            
        gap = 0
        for i in range(len(nums)-1):
            gap = max(gap, nums[i+1] - nums[i])
        return gap
        
    
    ### counting sort subroutine 
    def countSort(self, nums, divider, base = 10):
        # base == 10
        buckets = [[] for _ in range(base)]
        for n in nums:
            key = (n // divider) % base
            buckets[key].append(n)
        count = 0
        for i in range(base):
            for n in buckets[i]:
                nums[count] = n
                count += 1
    ### we can increase the bucket size of counting sort                
    def maximumGap(self, nums: List[int]) -> int:
        if(len(nums) <= 1):
            return 0
        maxx, minn = -math.inf, math.inf
        for n in nums:
            maxx = max(maxx, n)
            minn = min(minn, n)
        k = math.ceil((maxx - minn) / (len(nums) - 1)) # bucket_size
        
        buckets = [[math.inf, -math.inf, 0] for _ in range(len(nums))]
        if(k == 0):
            return 0
        for n in nums:
            n -= minn # so bucket index starts from zero
            key = n // k
            buckets[key][2] = 1
            buckets[key][0] = min(buckets[key][0], n)
