#bseds22032
#Abdul Rehman
#problem 2 part (a)




def is_prime(x):

 r  = 0
 for y in range (2,x):
     if (x%y==0):   
        return (False)
        r = 1
        break
 if r != 1:
     return (True)
    
    
    
x=int(input("enter a number:"))
print (is_prime(x))