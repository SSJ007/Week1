class Stack:
    def __init__(self):
        self.elements = []

    def push(self, val):
        self.elements.append(val)

    def pop(self):
        if self.elements:
            return self.elements.pop()
        else:
            return None

s=Stack()

while True:
    print("1.Push")
    print("2.Pop")
    print("3.Quit")
    user_input = int(input("Choose an option\n"))
    if user_input==1:
        val = int(input("Enter the value\n"))
        s.push(val)
    elif user_input==2:
        pop = s.pop()
        if pop==None:
            print("What do i pop? Fill the stack\n")
        else:
            print("There you go:",pop)
            print("")
    elif user_input==3:
        break
