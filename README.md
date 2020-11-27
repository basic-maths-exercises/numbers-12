# The decimal representation

By the end of the last exercise, we arrived at the set of rational numbers, which is closed under the operations of addition, subtraction and multiplication.  This set is also closed under division as long as we do not divide by zero.

In this task, I want to combine this knowledge about the sets of numbers with the earlier parts of this exercise, which discussed how we represent numbers.  In these previous tasks, we discussed how all the natural numbers  could be represented using the following sum:

![](https://render.githubusercontent.com/render/math?math=\sum_{n=0}^\infty\a_nA^n)

where each of the ![](https://render.githubusercontent.com/render/math?math=a_n) in this expression is a natural number that is less than ![](https://render.githubusercontent.com/render/math?math=A).  In this task, I want to consider what happens if we change the bottom limit in the sum as shown below:

![](https://render.githubusercontent.com/render/math?math=\sum_{n=-\infty}^\infty\a_nA^n)

To make this clear what this small change adds suppose that ![](https://render.githubusercontent.com/render/math?math=A) is 10 (i.e. that we are in boring old base 10).  The ![](https://render.githubusercontent.com/render/math?math=n=-1) term in this sum is then a natural number that is less than 10 multiplied by ![](https://render.githubusercontent.com/render/math?math=10^{-1}=\frac{1}{10}), the ![](https://render.githubusercontent.com/render/math?math=n=-2) term in the sum is a natural number that is less than 10 multiplied by ![](https://render.githubusercontent.com/render/math?math=10^{-2}=\frac{1}{100}), the ![](https://render.githubusercontent.com/render/math?math=n=3) term in the sum above is a natural number that is less than 10 multiplied by ![](https://render.githubusercontent.com/render/math?math=10^{-3}=\frac{1}{1000}) and so on.  In other words, the above sum is just a complicated way of representing the decimals numbers that you know and love.

To demonstrate that you have understood the ideas explained above I would like you to __complete the function called `getDecimalDigits`__ in `main.py`.  This code takes a real number, `x`, as input.  It should return a NumPy array with ten elements.  The zeroth element in this array should be set equal to the first digit after the decimal point in `x`, the first element of this array should be set equal to the second digit after the decimal point in `x` and so on.

   
