from time import sleep

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag(root):
    flag = True    
    q = [root]
    result = []
    while(q):
        lenq = len(q)
        temp = []
        stack = []
        for i in range(lenq):
            node = q.pop(0)
            if node:
                temp.append(node.val)
                stack.append(node)
        while stack:
            node = stack.pop()
            print("Stack", stack)
            if node:
                if flag:
                    q.append(node.right)
                    q.append(node.left)
                else:
                    q.append(node.left)
                    q.append(node.right)
        flag = not flag
        if temp:
            result.append(temp)
    return result


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
    print(zigzag(root))