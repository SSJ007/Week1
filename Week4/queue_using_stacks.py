class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):

        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):

        if len(self.s1) == 0:
            print("Queue is Empty")

        x = self.s1[-1]
        self.s1.pop()
        return x


q = Queue()
q.enQueue(50)
q.enQueue(20)
q.enQueue(33)

print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
