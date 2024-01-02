
          
#Part#06
def sumMatrix(a, b):
 
    sum=0
   
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):      
           a[i][j] = a[i][j]+b[i][j]      
    return (a)
 
a = [[ 5, 2, 2],
     [ 2, 5, 2 ],
     [ 2, 2, 5,]]
     
b = [[ 15, 6, 6],
     [ 6, 15, 6 ],
     [ 6, 6, 15 ]]
print (sumMatrix(a, b))