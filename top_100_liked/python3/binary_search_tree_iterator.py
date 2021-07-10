import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
​
    def __init__(self, root: TreeNode):
        self.it = self.dfs(root)
        while(root.right):
            root = root.right
        self.last = root
        self.cur  = None
    def next(self) -> int:
        self.cur = next(self.it)
        return self.cur.val
    
    def hasNext(self) -> bool:
        if(self.cur == self.last):
            return False
        return True
        
    def dfs(self, node):
        if(node == None):
            return
        yield from self.dfs(node.left)
        yield node
        yield from self.dfs(node.right)
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
