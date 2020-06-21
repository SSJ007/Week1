class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        return self.items.pop(0)


q = Queue()
while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Quit")
    user_input = int(input("Choose an option\n"))
    if user_input == 1:
        val = int(input("Enter the value\n"))
        q.enqueue(val)
    elif user_input == 2:
        if q.is_empty():
            print("Nothing in here\n")
        else:
            print("Take it:",q.dequeue())
            print("")
    elif user_input == 3:
        break
