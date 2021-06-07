class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        n = len(mat2[0])
        k = len(mat2)
        ans = [[0]*n for _ in range(m)] 
        sparse1 = self.getSparse(mat1, 0, m, k)
        sparse2 = self.getSparse(mat2, 1, n, k)
        for i in range(m):
            for j in range(n):
                sparse = sparse1[i] if len(sparse1[i]) < len(sparse2[j]) else sparse2[j]
                for k in sparse:
                    ans[i][j] += mat1[i][k] * mat2[k][j] 
        return ans
    def getSparse(self, mat, flag, m, k):
        sparse = []
        if(flag):
            for j in range(m):
                col = []
                for i in range(k):
                    if(mat[i][j]):
                        col.append(i)
                sparse.append(col)
        else:
            for i in range(m):
                row = []
                for j in range(k):
                    if(mat[i][j]):
                        row.append(j)
                sparse.append(row)
        return sparse
