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

global_leaf_level = -1

def check_level(root, level):
    global global_leaf_level
    if root == None:
        return True
    if not root.left and not root.right:
        if global_leaf_level != -1:
            return global_leaf_level==level
        else:
            global_leaf_level = level
    return check_level(root.left, level+1) and check_level(root.right, level+1)



def check(root):
    level = 0
    return check_level(root, level)

        
    

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(8)
    

    root.right = TreeNode(3)    
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(9)
    root.right.left.right = TreeNode(10)
    root.right.right.right = TreeNode(11)
    print(check(root))