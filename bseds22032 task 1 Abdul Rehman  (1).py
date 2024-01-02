def countdigit (n):
  count =1
  sum =0
  while (n>9):
      n=n//10
      sum=sum+n
      count =count+1 
  return ("sum is",sum)
n=int(input("enter a number"))
print (countdigit(n))