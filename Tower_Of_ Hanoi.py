def TowerOfHanoi(n , fr, to, temp):
    if n == 1:
        print ("Move disk 1 fr rod",fr,"to rod",to)
        return
    TowerOfHanoi(n-1, fr, temp, to)
    print ("Move disk",n,"fr rod",fr,"to rod",to)
    TowerOfHanoi(n-1, temp, to, fr)
(rod1, rod2, rod3)=input("Name the source, destination and auxiliary rods respectively\n").split()
n=int(input("Enter number of disks\n"))
TowerOfHanoi(n, rod1, rod2, rod3)
