'''
Given a binary tree, return the list of largest element in each level
'''

import collections
from tkinter.tix import Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def children_sum(root):

    def is_leaf(node):
        return not node.left and not node.right
    
    def node_value(node):
        if not node: return 0
        return node.val
    
    def dfs(root):
        if root == None:
            return True
        if is_leaf(root):
            return True
        return root.val == (node_value(root.left)+node_value(root.right)) and dfs(root.left) and dfs(root.right)
    
    return dfs(root)
        
    

if __name__ == "__main__":
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(6)
    print(children_sum(root))