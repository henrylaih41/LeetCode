# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
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
    def deserialize(self, s: str) -> NestedInteger:
        if(s[0] == "["):
            obj, _ = self.recursive(s, 1)
        else:
            obj, _ = self.deserialize_Integer(s, 0)
        return obj
        
    def recursive(self, s, i):
        nI = NestedInteger()
        while(i < len(s)):
            if(s[i] == "["):
                obj, i = self.recursive(s, i+1)
                nI.add(obj)
            elif(s[i] == "]"):
                return nI, i+1
            elif(s[i] == ","):
                i += 1
            ### "-" or isdigit()
            else:
                obj, i = self.deserialize_Integer(s, i)
                nI.add(obj)
        ### we will never reach here, since we must encounter a ] first
        
    def deserialize_Integer(self, s, i):
        sign = -1 if s[i] == "-" else 1
        cur = 0
        if(s[i] == "-"):
            i += 1
        while(i < len(s) and s[i].isdigit()):
            cur = cur * 10 + sign * int(s[i])
            i += 1
        return NestedInteger(cur), i
                    
        
        
