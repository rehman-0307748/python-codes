x =int(input("enter a number:"))
y =int(input("enter a number:"))
for i in range (x,y):
   p=1
   for c in range (2,i):
       if (i%c==0):
          p=0
          break
   if p!=0:
      print(i)  