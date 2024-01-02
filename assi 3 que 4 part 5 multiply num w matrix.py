#Abdul Rehman 
#bseds 22032
#question 4 part (5)



def multiplynum(n):

 list=[[3, 4, 5], [6, 4, 1], [3, 5, 5]]

 for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        list[i][j]=list[i][j]*n
 return (list)
n=int(input("enter the number:"))
print (multiplynum(n))