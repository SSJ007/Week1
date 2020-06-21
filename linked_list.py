class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()

    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total

    def display(self):
        elems=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
        print()

    def get(self,index):
        if index>=self.length() or index<0: # added 'index<0' post-video
            print("Enter a valid index\n")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index:
                print(cur_node.data)
                print()
                return None
                #return cur_node.data
            cur_idx+=1

    def erase(self,index):
        if index>=self.length() or index<0: # added 'index<0' post-video
            print("Enter a valid index\n")
            return
        cur_idx=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_idx==index:
                last_node.next=cur_node.next
                return
            cur_idx+=1

ll=linked_list()

while True:
    print("1.Insert in linked list")
    print("2.Delete a value")
    print("3.Search a value")
    print("4.Display the linked list")
    print("5.Quit")
    user_input = int(input("Choose an option\n"))
    if user_input == 1:
        val = int(input("Enter the value\n"))
        ll.append(val)
    elif user_input == 2:
        val = int(input("Enter the index value to be deleted\n"))
        ll.erase(val)
    elif user_input == 3:
        val = int(input("Enter the index value to be searched\n"))
        ll.get(val)
    elif user_input == 4:
        ll.display()
    elif user_input == 5:
        break
