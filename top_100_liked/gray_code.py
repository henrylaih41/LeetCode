class Solution:
    def grayCode(self, n: int) -> List[int]:
        base = [0]
        for i in range(n):
            j = len(base) - 1
            while(j >= 0):
                base.append(base[j] + 2 ** i)
                j -= 1
        return base
            
        
