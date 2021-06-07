from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if(root == None):
            return []
        mincount, maxcount = math.inf, -math.inf
        columns = defaultdict(lambda: [])
        result = []
        q = deque([(root, 0)])
        
        while(len(q)):
            node, count = q.popleft()
            mincount = min(mincount, count)
            maxcount = max(maxcount, count)
            columns[count].append(node.val)
            if(node.left):
                q.append((node.left, count-1))
            if(node.right):
                q.append((node.right, count+1))
        
        for i in range(mincount, maxcount+1):
            if(len(columns[i])):
                result.append(columns[i])
        return result
    
    """ 
    dfs won't work because we have to print from top to bottom
    def dfs(self, node, count):
        if(node == None):
            return
        self.columns[count].append(node.val)
        self.dfs(node.left, count-1)
        self.dfs(node.right, count+1)
    """
