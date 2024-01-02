#Abdul Rehman 
#bseds 22032
#question 4 part (2)



def add_num(n):

 list=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

 for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        list[i][j]+=n
 return (list)

print (add_num(3))