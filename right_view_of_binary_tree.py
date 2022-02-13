import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
        res = []
        q = collections.deque([root])
        
        while(q):
            rightside = None
            lenq = len(q)
            for i in range(lenq):
                node = q.popleft()
                if node:
                    # at end of for loop, rightside will have rightmost node
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside.val)
        return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(rightSideView(root))