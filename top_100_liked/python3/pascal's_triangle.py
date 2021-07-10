class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1], [1,1]]
        if(numRows <= 2):
            return rows[:numRows]
        for i in range(2, numRows):
            rows.append([1])
            for j in range(len(rows[-2])-1):
                rows[-1].append(rows[-2][j]+rows[-2][j+1])
            rows[-1].append(1)
        
        return rows
