#bseds 22032
#task 4
#Abdul Rehman




def squareRoot(a):


  guess=a/2
  while abs ((guess*guess)-a)>0.01:
    guess =(guess+a/guess)/2
  return (guess)

a=float(input ("enter a number:"))
print (squareRoot(a))