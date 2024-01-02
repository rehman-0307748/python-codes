#bseds 22032 
#Abdul Rehman
# task 1 part (a)



def countdigit (n):
  count =1
  sum =0
  while (n>9):
      n=n//10
      sum=sum+n
      count =count+1 
  return ("total number of digits is ",count,)


n=int(input("enter a number"))
print (countdigit(n))