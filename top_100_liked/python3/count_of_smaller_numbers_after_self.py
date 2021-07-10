            self._point_update(r+1, self.nums[r+1]-value)
        
class component:
    def __init__(self, pos, value):
        self.value, self.pos = value, pos
    
    def __le__(self, ot):
        return self.value <= ot.value
    
    def __str__(self):
        return "({0}, {1})".format(self.value, self.pos)
​
class Solution: 
    def BITcountSmaller(self, nums: List[int]) -> List[int]:
        minn, maxx = math.inf, -math.inf
        for i in range(len(nums)):
            minn = min(nums[i], minn)
            maxx = max(nums[i], maxx)
        for i in range(len(nums)):
            nums[i] += (-minn + 1)
        maxx += (-minn + 1)
        bit = BIT(maxx)
        count = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            count[i] = bit.query(nums[i])
            bit.range_update(1, nums[i]+1, maxx)
            
        return count
    
    def countSmaller(self, nums):
        for i in range(len(nums)):
            nums[i] = component(i, nums[i])
        count = [0]*len(nums)
        self.mergeSort(nums, 0, len(nums)-1, count)
        return count
    def mergeSort(self, nums, l, r, count):
        if(l == r):
            return 
        
        mid = (l+r)//2
        self.mergeSort(nums, l, mid, count)
        self.mergeSort(nums, mid+1, r, count)
        
        left = [0]*(mid-l+1)
        right = [0]*(r-mid)
        ### merge
        for i in range(l, mid+1):
            left[i-l] = nums[i]
        for i in range(mid+1, r+1):
            right[i-mid-1] = nums[i]
        i, j, k = 0, 0, l
        while(i < len(left) and j < len(right)):
            if(left[i].value <= right[j].value):
                nums[k] = left[i]
                count[left[i].pos] += j
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while(i < len(left)):
            nums[k] = left[i]
            count[left[i].pos] += j
            i += 1
            k += 1
        while(j < len(right)):
            nums[k] = right[j]
            j += 1
            k += 1
      
        
