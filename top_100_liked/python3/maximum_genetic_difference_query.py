from collections import defaultdict
max_bit = 18 ### since val <= 10^5 we can do this to avoid TLE (the time constant is very strict)     
class TrieNode:
    def __init__(self):
        self.children = {}
        self.refcnt = 0  
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, val):
        curr = self.root
        for i in range(max_bit, -1, -1):
            bit = 1 if (val & (1 << i)) else 0
            if(bit not in curr.children):
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
            curr.refcnt += 1
    
    def delete(self, val):
        curr = self.root
        arr = []
        for i in range(max_bit, -1, -1):
            bit = 1 if(val & (1 << i)) else 0
            arr.append((bit, curr))
            curr = curr.children[bit]
            curr.refcnt -= 1
        for i in range(max_bit, -1, -1):
            bit, curr = arr[i]
            if(curr.children[bit].refcnt == 0):
                del curr.children[bit]
            else:
                break
                
    def query(self, val):
        curr = self.root
        maxx = 0
        for i in range(max_bit, -1, -1):
            bit = 1 if(val & (1 << i)) else 0
            inv_bit = 1 - bit
            if(inv_bit in curr.children):
                maxx |= (1 << i)
                curr = curr.children[inv_bit]
            else:
                curr = curr.children[bit]
        return maxx            
​
class Solution:
    ### naive solution O(n*q) n = len(parents) q = len(queries)
    ### O(n) solution, we do a dfs on the tree, during the dfs we insert the visited node, remove it after dfs, 
