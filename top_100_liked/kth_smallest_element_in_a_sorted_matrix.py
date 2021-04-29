from heapq import heappush, heappop
class Solution:
    ### min heap method
    def v1kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        row_pt = [0] * n
        heap = [] # min heap
        for i in range(min(n,k)):
            heappush(heap, (matrix[i][row_pt[i]], i))
            row_pt[i] += 1
        
        while(k != 1):
            _, i = heappop(heap)
            if(row_pt[i] < n):
                heappush(heap, (matrix[i][row_pt[i]], i))
                row_pt[i] += 1
            k -= 1
        return heap[0][0]
​
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        l, r = matrix[0][0], matrix[n-1][n-1]
        
        while(l < r):
            mid = (l+r)//2
            cnt, flag = self.countSmaller(matrix, mid)
            if(cnt == k and flag):
                return mid
            elif(cnt >= k): # this equal is important
                r = mid
            else:
                l = mid + 1
        return l ### if kth element is repeated (kth kth kth kth)
    
    def countSmaller(self, matrix, v):
        n, maxx = len(matrix), -math.inf
        row, col, cnt = 0, n-1, 0
        while(row != n and col >= 0):
            if(v >= matrix[row][col]):
                maxx = max(matrix[row][col], maxx)
                cnt += col+1
                row += 1
            else:
                col -= 1
        return cnt, (maxx == v)
            
