# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if(root == None):
            return result
        s, dirr = [root], 0
        while(len(s) != 0):
            result.append([])
            for n in s:
                result[-1].append(n.val)
            ns = []
            while(len(s) != 0):
                n = s.pop()
                if(dirr):
                    if(n.left):
                        ns.append(n.left)
                    if(n.right):
                        ns.append(n.right)
                else:
                    if(n.right):
                        ns.append(n.right)
                    if(n.left):
                        ns.append(n.left)
            s = ns
            dirr = not dirr
        return result
