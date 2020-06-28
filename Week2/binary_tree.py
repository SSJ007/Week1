class BT:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def set_root(self, data):
        self.data = data

    def inorder_traversal(self):
        if self.left is not None:
            self.left.inorder_traversal()
        print(self.data, end=' ')
        if self.right is not None:
            self.right.inorder_traversal()

    def insert_left(self, new_node):
        self.left = new_node

    def insert_right(self, new_node):
        self.right = new_node

    def search(self, data):
        if self.data == data:
            return self
        if self.left is not None:
            temp =  self.left.search(data)
            if temp is not None:
                return temp
        if self.right is not None:
            temp =  self.right.search(data)
            return temp
        return None


binary_tree = None

#print('no duplicate datas')
print('1. Insert data at root')
print('2. Insert data left of some data')
print('3. Insert data right of some data')
print('4. Quit')

while True:
    print('Inorder traversal of binary tree: ', end='')
    if binary_tree is not None:
        binary_tree.inorder_traversal()
    print()

    choice = int(input('Choose an option'))

    if choice == 1:
        data = int(input('Enter the value'))
        new_node = BT(data)
        binary_tree = new_node
    if choice == 2 or choice == 3:
            data = int(input('Enter the value'))
            new_node = BT(data)
            positional_data = int(input('Left or Right of which value?'))
            ref_node = None
            if binary_tree is not None:
                ref_node = binary_tree.search(positional_data)
            if ref_node is None:
                print('No such value exists')
                continue
            if choice==2:
                ref_node.insert_left(new_node)
            elif choice==3:
                ref_node.insert_right(new_node)

    if choice == 4:
        break
