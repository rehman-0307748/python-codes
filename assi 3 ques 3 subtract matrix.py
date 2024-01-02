# bseds 22032 
# Abdul Rehman 
# question # 3

def subtraction(m1,m2):
    new=[]
    for i in range(0,len(m1)):
        new.append(m1[i]-m2[i])
    return new
m1=[[4,4],[4,5]]
m2=[[5,3],[3,4]]
t=[]
for i in range(0,len(m1)):
    t.append(subtraction(m1[i],m2[i]))
print(t)