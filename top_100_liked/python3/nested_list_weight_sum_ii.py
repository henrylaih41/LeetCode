#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
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
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        summ = []
        for ni in nestedList:
            self.dfs(ni, 0, summ)
        
        result = 0
        for i, s in enumerate(summ):
            result += (s * (len(summ) - i))
        return result
    
    def dfs(self, NI, level, summ):
        if(level == len(summ)):
            summ.append(0)
        
        if(NI.isInteger()):
            summ[level] += NI.getInteger()
        else:
            for ni in NI.getList():
                self.dfs(ni, level+1, summ)
        
        
        
        
        
