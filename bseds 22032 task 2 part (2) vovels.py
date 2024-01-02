#bseds 22032
#task 2
#Abdul Rehman 

def countvovel(vo):
   vovel ="aeiouAEIOU"
   count =0
   for i in vo :
       if i in vovel:
         count+=1
   return count


vo =input ("enter a string:")
print (countvovel(vo))