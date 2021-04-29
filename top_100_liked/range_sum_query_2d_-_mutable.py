    
    ###[1-]
    def _query(self, x, h1, h2):
        summ = 0
        while(x > 0):
            summ += self.bit_sums[x].query(h1, h2)
            #print(x, h1, h2, summ)
            x -= (x & -x)
        return summ
    
### This method should have O(logN + logM) complexity
### Try to implement next time (handle the one stripe edge case seperately)
class TreeNode2D:
    def __init__(self, x1, y1, x2, y2, value=None):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.x = [x1, (x1+x2)//2, x2]
        self.y = [y1, (y1+y2)//2, y2]
        self.child = [None]*4 # hard code here 4 = 2 x 2 (2D)
        self.parent = None
        self.summ = value
    def getPoint(self, idx):
        return [self.x[idx % 3], self.y[idx//3] ] # 3 == len(self.x) we hardcode here
    
    ### we ensure (x, y) is in the [x1, y1] ~ [x2, y2] region
    ### the return value correspond to the quadrant
    ### |0| 1|
    ### |2| 3|
    def pointRegion(self, x, y):
        if(x <= self.x[1] and y <= self.y[1]):
            return 0  
        if(x > self.x[1] and y <= self.y[1]):
            return 1
        if(x <= self.x[1] and y > self.y[1]):
            return 2
        if(x > self.x[1] and y > self.y[1]):
            return 3
        print("ERROR in Point Region")
    
class segmentTree2D:
    def __init__(self, matrix):
        self.matrix = matrix
        self.root   = self.buildTree(0,0,len(matrix[0])+1,len(matrix)+1)
    
    def buildTree(self, x1, y1, x2, y2, matrix):
        if(x1 == x2 - 1 and y1 = y2 - 1):
            return TreeNode2D(x1, y1, x2, y2, matrix[x1][y1])
        x12, y12 = (x1+x2)//2, (y1+y2)//2
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
