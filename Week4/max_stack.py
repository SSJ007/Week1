class MaxStack:
    def __init__(self):
        self._stack = []
        self._max_values =[]

    def push(self, x):
        self._stack.append(x)
        if not self._max_values:self._max_values.append(x)
        else:
            this_max = max(x, self._max_values[-1])
            self._max_values.append(this_max)

    def pop(self):
        self._max_values.pop()
        return self._stack.pop()

    def peekMax(self):
        if self._stack:
            return self._max_values[-1]

s=MaxStack()
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Maximum value")
    print("4.Quit")
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
        print(s.peekMax())
    elif user_input==4:
        break
