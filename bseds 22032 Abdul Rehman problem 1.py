#problem 1




x=int(input("enter the number:"))
y=int (input("enter second number:"))
sum=0
if (x<y):
  for x in range (x+1,y):
     if (x%2!=0):
        print ("odd number between",x,'and',y,'is',x)
        sum =sum+x
print ("sum of all odd numbers is =",sum)