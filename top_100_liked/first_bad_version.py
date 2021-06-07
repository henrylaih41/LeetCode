# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
​
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n+1
        while(l < r):
            mid = (l+r)//2
            if(isBadVersion(mid)):
                if(mid == 1 or not isBadVersion(mid-1)):
                    return mid
                else:
                    r = mid
            else:
                l = mid + 1
        
                
