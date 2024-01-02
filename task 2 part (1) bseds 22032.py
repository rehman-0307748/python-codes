#bseds 22032
#Abdul Rehman
#task 2




def space (a):
   count= 0
   for i in range (0,len(a)):
       if a[i]==" ":
          count+=1
   return (count)
a=input ("enter a string:")
print (space (a))