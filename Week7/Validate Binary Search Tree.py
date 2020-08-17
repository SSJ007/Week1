class Solution:
    def isValidBST(self, root):
        stack = []
        nodes = []
        while True:
          while root:
            stack.append(root)
            root = root.left
          if not stack:
            return True
          right_root = stack.pop()
          if nodes and right_root.val <= nodes.pop():
            return False
          nodes.append(right_root.val)
          root = right_root.right
