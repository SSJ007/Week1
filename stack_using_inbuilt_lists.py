s=[]
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Quit")
    user_input = int(input("Choose an option\n"))
    if user_input==1:
        val = int(input("Enter the value\n"))
        s.append(val)
    elif user_input==2:
        if s:
            print("There you go:",s.pop())
            print("")
        else:
            print("What do i pop? Fill the stack first\n")
    elif user_input==3:
        break
