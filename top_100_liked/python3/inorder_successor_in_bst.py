# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if(p == self.getBiggest(root)):
            return None
        ### smallest of right subtree
        if(p.right):
            return self.getSmallest(p.right)
        return self.findParent(root, p)
    
    def findParent(self, root, p):
        track = [root]
        while(root != p):
            if(p.val > root.val):
                root = root.right
            else:
                root = root.left
            track.append(root)
        while(track[-1].val <= p.val):
            track.pop()
        return track[-1]
    
    ### Brute force
    def inorder(self, root):
        if(root == None):
            return
        self.inorder(root.left)
        if(self.flag and self.ans == None):
            self.ans = root
            return
        if(root == self.p):
            self.flag = 1
        self.inorder(root.right)
            
    def getBiggest(self, root):
        while(root.right != None):
            root = root.right
        return root
    
    def getSmallest(self, root):
        while(root.left != None):
            root = root.left
        return root
