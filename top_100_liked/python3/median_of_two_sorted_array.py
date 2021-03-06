import math
from typing import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ### A is the longer array
        A = nums1 if len(nums1) >= len(nums2) else nums2
        B = nums1 if len(nums1) <  len(nums2) else nums2
        m, n = len(A), len(B)
        target, odd = (m+n+1)//2, (m+n)%2
        # edge case
        if(m == 0): # both 0
            return 0
        if(n == 0):
            return A[target-1] if(odd) else (A[target-1] + A[target])/2
        minn, maxx = target - n - 1, target - 1
        while(True):
            mid = (minn + maxx)//2
            bpt = target - mid - 2
            a = -math.inf if mid < 0 else A[mid]
            a_ = math.inf if mid+1 >= m else A[mid+1]
            b = -math.inf if (bpt < 0 or bpt >= n) else B[bpt]
            b_ = math.inf if bpt+1 >= n else B[bpt+1]
            
            if(b_ >= a and a_ >= b and bpt < n):
                if(odd):
                    return max(a, b)
                return (max(a,b) + min(a_,b_))/2
            
            if(b_ < a):
                maxx = mid - 1
            elif(a_ < b or bpt >= n):
                minn = mid + 1  
        
class SSolution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # let A be the bigger array, we do binary search on it
        A = nums1 if len(nums1) >= len(nums2) else nums2
        B = nums1 if len(nums1) <  len(nums2) else nums2
        m, n = len(A), len(B)
        B.append(math.inf) # for edge case purpose
        A.append(math.inf)
        target, odd = (m+n+1)//2, (m+n)%2
        ### edge case
        if(n == 0):
            if(m == 0):
                return 0
            else:
                if(m % 2 == 0):
                    return (A[m//2-1] + A[m//2])/2
                else:
                    return A[m//2]
        ### edge case (very important...)
        if(A[target - 1] <= B[0]): # all A
            return A[target-1] if odd else ((A[target-1] + min(A[target],B[0]))/2)
        if(n >= target and B[target-1] <= A[0]): # all B   
            return B[target-1] if odd else ((B[target-1] + min(B[target],A[0]))/2)
        ### binary search
        minn, maxx = 0, target - 2 # [minn, maxx] = [-1, target-1] target <= m
        ### mid, bpt >= 0 in following codes
        while(True): # we can always find the median, return when found
            mid = (minn + maxx)//2
            bpt = target - mid - 2 # bpt range is [-1, n-1]
            if(bpt >= n or A[mid+1] < B[bpt]):
                minn = mid+1
            elif(B[bpt+1] < A[mid]):
                maxx = mid-1
            ### found
            elif((mid+1 >= m or A[mid+1] >= B[bpt]) and (bpt+1 >= n or B[bpt+1] >= A[mid])):
                if((m+n) % 2 == 1):
                    return max(A[mid], B[bpt])
                else:
                    if(mid+1 < m and bpt+1 < n):
                        nxt_element = min(A[mid+1], B[bpt+1])
                    elif(mid + 1 >= m):
                        nxt_element = B[bpt+1]
                    else:
                        nxt_element = A[mid+1]
                    return (max(A[mid], B[bpt]) + nxt_element)/2

s = Solution()
s.findMedianSortedArrays([1,2],[3,4])
