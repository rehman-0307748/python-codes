a=int(input("enter a number :"))
first=0
print (first)
second=1
print (second)
sum=1
for count in range (a-2):
   third = first+second
   sum+=third
   print (third)
   first = second
   second = third
print ("sum is ",sum)