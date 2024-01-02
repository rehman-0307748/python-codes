#Abdul Rehman 
#bseds 22032
#quetion 4 part 4


def diagonalSum(a, n):
 
    sum=0
   
    for i in range(0,n):
        for j in range(0, n):
 
            if (i == j):
                sum = sum+a[i][j]
               
    return sum
 
a = [[ 5, 2, 2],
     [ 2, 5, 2 ],
     [ 2, 2, 8]]
print ("your diognal sum is =",diagonalSum(a,3))