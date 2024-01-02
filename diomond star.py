x =int(input("enter a number:"))
for i in range (0,x):
    for j in range (0,x-i-1):
        print (end=" ")
    for p in range (0,i+1):
        print ("* ",end="")
    print ()
for i in range (x-1,0,-1):
    for j in range (x,i,-1):
        print (end=" ")
    for p in range (0,i):
        print ("* ",end="")
    print ()