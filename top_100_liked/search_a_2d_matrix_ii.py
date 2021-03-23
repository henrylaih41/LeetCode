class Solution:
    def BinarysearchMatrix(self, matrix, target):
        r, n, m = 0, len(matrix), len(matrix[0])
        while(r < n and matrix[r][0] <= target):
            if(self.binary_s(0, m, matrix[r], target)):
                return True
            r += 1
        return False
        
        
    def binary_s(self, l, r, row, target):
        while(l < r):
            mid = (l+r)//2
            if(row[mid] == target):
                return True
            elif(row[mid] > target):
                r = mid
            else:
                l = mid + 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       ### We start from the upper right corner
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m-1
        while(i < n and j >= 0):
            if(matrix[i][j] == target):
                return True
            elif(matrix[i][j] > target):
                j -= 1
            else:
                i += 1
        return False
    
