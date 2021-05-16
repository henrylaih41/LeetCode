class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        ### binary search
        l, r = 0, m*n
        
        while(l < r):
            mid = (l+r)//2
            i, j = mid // n, mid % n
            if(matrix[i][j] == target):
                return True
            elif(matrix[i][j] > target):
                r = mid
            else:
                l = mid + 1
        return False
