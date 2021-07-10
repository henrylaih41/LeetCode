# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Codec:
    # recursive serialize
    # root, left subtree..., right subtree ....,
    def rser(self, root, data):
        if(root == None):
            data.append("None,")
            return
        data.append(str(root.val) + ",")
        self.rser(root.left, data)
        self.rser(root.right, data)
    def serialize(self, root):
        data = []
        self.rser(root, data)
        return "".join(data)
        
        
    def rdeser(self, data):
        if(data[0] == "None"):
            data.pop(0)
            return None
        root = TreeNode(int(data[0]))
        data.pop(0)
        root.left = self.rdeser(data)
        root.right = self.rdeser(data)
        
        return root
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        return self.rdeser(data)
        
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
