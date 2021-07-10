# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr = []
        while(head):
            arr.append(head.val)
            head = head.next
        
        return self.build_balance(arr, 0, len(arr)-1)
        
    def build_balance(self, arr, i, j):
        if(i > j):
            return None
        if(i == j):
            return TreeNode(arr[i])
        mid = (i + j) // 2
        root = TreeNode(arr[mid])
        root.left = self.build_balance(arr, i, mid-1)
        root.right = self.build_balance(arr, mid+1, j)
        
        return root
    
    ### simulate inorder
    def sortedListToBST(self, head):
        self.head = head
        count = 0
        while(head):
            count += 1
            head = head.next
        return self.build_tree(1, count)
    
    def build_tree(self, i, j):
        if(i > j):
            return None
        
        if(i == j):
            root = TreeNode(self.head.val)
            self.head = self.head.next
            return root
        root = TreeNode()
        mid = (i+j)//2
        root.left = self.build_tree(i, mid-1)
        root.val = self.head.val
        self.head = self.head.next
        root.right = self.build_tree(mid+1, j)
        
        return root
        
