class Solution:
    ### Q: why can we greedly put the nodes?
    ### A: (maybe) if we can put the node, then the node can only be put at
    ### that position, the other possible would not be valid because we dfs left to right
    ### if the node can be put in the left subtree than it cannot be put in the right subtree
    ### the last go-left parent and go-right parent would bound
    ### the value of the current node
    def verifyPreorder(self, preorder: List[int]) -> bool:
        self.i = 0
        self.dfs(preorder, -math.inf, math.inf)
        return (self.i == len(preorder))
    
    def dfs(self, preorder, minn, maxx):
        if(self.i == len(preorder)):
            return
        val = preorder[self.i]
        if(val < maxx and val > minn):
            self.i += 1
            ### go left
            self.dfs(preorder, minn, val)
            ### go right
            self.dfs(preorder, val, maxx)
            
    ### stack version (magic)
    ### not sur why this works
    ### we know that the right subtrees only get larger
    ### doesn't really put the node in the right position
    def verifyPreorder(self, preorder):
        lower_bound = -math.inf
        stack = []
        for val in preorder:
            if(val < lower_bound):
                return False
            while(len(stack) and val > stack[-1]):
                lower_bound = stack.pop()
            stack.append(val)
        return True
