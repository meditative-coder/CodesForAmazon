'''
Given a binary tree, return the list of largest element in each level
'''

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def largest_in_each_level(root):
    hash = {}
    q = collections.deque([root])
    maximum_in_each_level = list()
    while(q):
        lenq = len(q)
        max_in__current_level = -float('inf')
        for i in range(lenq):
            node = q.popleft()
            if node:
                max_in__current_level = max(max_in__current_level, node.val)
                q.append(node.left)
                q.append(node.right)
        maximum_in_each_level.append(max_in__current_level)
    return maximum_in_each_level[:-1]
        
    

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
    print(largest_in_each_level(root))