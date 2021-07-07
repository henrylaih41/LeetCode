class Solution:
    def comb(self, n, i):
        ### C(5, 1) = 5 / 1, C(5, 2) = 5 * 4 / 2
        ### C(n, i) = n! / (n-i)! / i! = n * ... * n - i + 1 / i!
        if(i == 0 or i == n):
            return 1
        
        
    def getRow(self, rowIndex: int) -> List[int]:
        ### 0 row is 1
        ### 1 row is C(1, 0) C(1, 1)
        ### 2 row is C(2, 0), C(2,1), C(2,2)
        result = []
        for i in range(rowIndex+1):
            if(i == 0 or i == rowIndex):
                result.append(1)
            else:
                result.append(result[-1] * (rowIndex-i+1) // i)
        
        return result
