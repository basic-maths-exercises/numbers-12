import numpy as np

def getDecimalDigits( x ) : 
  # Your code goes here


# You don't need to ajust the code here.  This allows you to test the function
# that you have written above.
for i in range(10) : 
  rand = np.random.uniform(0,20)
  print("The first 10 points after the decimal point in", rand, "are", 
  getDecimalDigits(rand))
