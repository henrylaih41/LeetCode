# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if(root == None):
            return []
        s = [[root, 0]] ### the recursive stack
        result = []
        while(len(s)):
            node, v = s[-1]
            if(v == 0):
                ### preorder here
                s[-1][1] = 1
                if(s[-1][0].left != None):
                    s.append([s[-1][0].left, 0])
            elif(v == 1):
                ### inorder here
                s[-1][1] = 2
                if(s[-1][0].right != None):
                    s.append([s[-1][0].right, 0])
            elif(v == 2):
                ### postorder here
                node, v = s.pop()
                result.append(node.val)
        return result
