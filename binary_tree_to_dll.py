'''
Given a binary tree, find the diameter of the binary tree
Diameter of Binary Tree: Longest path between any 2 nodes
'''

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = None
        self.head = None
    def btodll(self,root):
        if root==None:
            return self.head
        self.btodll(root.left)
        if self.prev==None:
            self.head = root
        else:
            self.prev.right = root
            root.left = self.prev
        self.prev = root
        self.btodll(root.right)   
    

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)    
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right.left = TreeNode(10)
    root.right.right.right = TreeNode(11)
    obj = Solution()
    obj.btodll(root)
    h = obj.head
    while(h):
        print(h.val)
        h = h.right