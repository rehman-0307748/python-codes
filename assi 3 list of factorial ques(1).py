# bseds 22032 
# Abdul Rehman 
# question # 1

def factorial(x):
  f=1
  for i in range (1,x+1):
     f=f*i
  return f 

p=[]
x=[0,4,5]
for y in range (0,len(x)):
    factorial(x[y])
    p.append (factorial(x[y]))
    
print (p)