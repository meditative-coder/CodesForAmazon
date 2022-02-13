'''
Given a binary tree, return the top view of tree
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def bottomView(root):
    hash = {}
    q = [(root, 0)]
    if root:
        hash[0] = root.val
    bfs = []
    while(q):
        lenq = len(q)
        for i in range(lenq):
            item = q.pop(0)
            node = item[0]
            hd = item[1]
            if node:
                hash[hd] = node.val
                bfs.append(node.val)
                q.append((node.left, hd-1))
                q.append((node.right, hd+1))
    return [hash[key] for key in sorted(hash)]
        
    

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
    print(bottomView(root))