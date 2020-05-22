#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) I believe that this function operates under an linear time increase (O(n)). a is increasing by n*n for every iteration, so I think that nullifies the n*n on the other side, leaving only a < n

b) I think that this function is- at its worst- O(n^2). It operates between linear and exponential, as values grow from an initial of near 2n to 3n to 4n and so on. This in itself sounds linear in its root, but since the growth is increasing at an increasing rate, it has to be worst-case scenario exponential

c) This is a linear function (O(n)). we know this because we are working towards a base case of 0, moving 1 unit closer with each call of the function. Thus, the time grows directly related to n.

## Exercise II

assuming we have an n story building and f floor that will be the highest possible drop, I think the most efficient solution would be to start at the n/2 floor. If it does break, we have eliminated all of the higher floors. if it doesn't break, we have eliminated all of the lower floors. from there we would continue to test whichever direction we need to go (higher if it doesn't break, lower if it does), until we have narrowed it down to the exact floor it will not break. This would maintain a time complexity of O(log n).
