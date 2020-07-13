class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, node):
        if self.key > node.key:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        elif self.key < node.key:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def inorderRecursive(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.inorder()

    def preorderRecursive(self):

        print(self.key, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def postorderRecursive(self):

        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.key, end=' ')


class BSTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root is not None:
            self.root.inorderRecursive()

    def preorder(self):
        if self.root is not None:
            self.root.preorderRecursive()

    def postorder(self):
        if self.root is not None:
            self.root.postorderRecursive()

    def add(self, key):
        new_node = BSTNode(key)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)


bstree = BSTree()

print('1. Add a value')
print('2. Inorder traversal')
print('3. Preorder traversal')
print('4. Postorder traversal')
print('5. Quit')

while True:
    choice = int(input('Choose an option\n'))

    if choice == 1:
        key = int(input('Enter the value: '))
        bstree.add(key)
    elif choice == 2:
        print('Inorder traversal: ', end='')
        bstree.inorder()
        print()
    elif choice == 3:
        print('Preorder traversal: ', end='')
        bstree.preorder()
        print()
    elif choice == 4:
        print('Postorder traversal: ', end='')
        bstree.postorder()
        print()
    elif choice==5:
        break
