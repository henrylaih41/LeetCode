# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
### O(logn*logn)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        l, r = self.countLevel(root)
        if(l == r):
            return (1 << (l + 1)) - 1
        return self.countLast(root, 0, l) + (1 << (r+1)) - 1
    
    def countLevel(self, root):
        left, right = root.left, root.right
        lcount, rcount = 0, 0
        
        while(left):
            left = left.left
            lcount += 1
        while(right):
            right = right.right
            rcount += 1
​
        return lcount, rcount
        
    def countLast(self, root, start, end):
        if(root == None):
            return 0
        if(start == end):
            return 1
        lcount, rcount = self.countLevel(root)
        if(lcount == rcount):
            if(start + lcount == end):
                return (1 << lcount)
            else:
                return 0
            
        return self.countLast(root.left, start+1, end) + self.countLast(root.right, start+1, end)
