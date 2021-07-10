"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
​
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if(node == None):
            return node
        visited = set()
        return self.dfs(node, visited)
    
    def dfs(self, node, visited):
        visited.add(node)
        node.clone = Node(node.val)
        for n in node.neighbors:
            if(n not in visited):
                neigh = self.dfs(n, visited)
            else:
                neigh = n.clone
            node.clone.neighbors.append(neigh)
        return node.clone
    
