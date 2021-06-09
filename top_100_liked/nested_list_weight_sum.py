#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
​
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.summ = 0
        for n in nestedList:
            if(n.isInteger()):
                self.summ += n.getInteger()
            else:
                self.recur(n, 1)
        return self.summ
        
        
    def recur(self, ns, depth):
        #if(nestedList.isInteger()):
        #    self.summ += nestedList.getInteger() * depth
        #    return
        if(ns.isInteger()):
            self.summ += ns.getInteger() * depth
            return    
        for n in ns.getList():
            self.recur(n, depth+1)
        
