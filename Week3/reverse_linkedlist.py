class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


linked_list = LinkedList()
#linked_list.push(20)
#linked_list.push(4)
#linked_list.push(15)
#linked_list.push(85)

size = int(input("Enter the size of linked list\n"))
for _ in range(size):
    linked_list.push(int(input("Enter the value: ")))
linked_list.printList()
linked_list.reverse()
print("\nReversed Linked List")
linked_list.printList()
