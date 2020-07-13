#To check if the binary tree is height balanced
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def isHeightBalanced(root, isBalanced=True):

    if root is None or not isBalanced:
        return 0, isBalanced

    left_height, isBalanced = isHeightBalanced(root.left, isBalanced)

    right_height, isBalanced = isHeightBalanced(root.right, isBalanced)

    if abs(left_height - right_height) > 1:
        isBalanced = False

    return max(left_height, right_height) + 1, isBalanced


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    if isHeightBalanced(root)[1]:
        print("Yes")
    else:
        print("No")
