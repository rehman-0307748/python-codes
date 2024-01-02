#bseds22032 
# Abdul Rehman
# problem 1 part (2)





def sumnum(n):


  sum =0
  while (n>0):
      sum =sum+n%10
      n=n//10
  return sum


n=int(input("enter a number:"))
print (sumnum (n))