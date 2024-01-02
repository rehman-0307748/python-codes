#bseds 22032
#task 3
#Abdul Rehman

def prime (a):
   for i in range (2,a):
       if a%i==0 :
          return False 
   return True 

 
def countprime (start,end):
    count =0
    for v in range (start , end ):
        if prime (v) :
           count+=1
    return count

start =int (input("enter a starting number:"))
end =int(input("enter a ending number:")) 
print (countprime(start,end))
   



           
 


    