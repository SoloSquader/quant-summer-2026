# Day 1 Probability

## Problem 1: You flip 3 fair coins. What is the probability of getting exactly 2 heads?

There are three instances of flipping: the first, second, and third flip. Each instance has 2 different outcomes: either heads of tails. 


Therfore, there are 2 * 2 * 2 = 8 different permutations of flips(since order matters). We need to find how many of those permutations have exactly 2 heads. 
Listing:


1. HHT
2. HTH
3. THH


It seems no further permutations are possible. Therfore, the probability is 3/8.


## Problem 2: You roll two fair six-sided dice. What is the probability that the sum is 6?

The same logic applies from the previous question: Find the amount of possible permutations, and then find the amount of permutations that satisfy the problem's condition. 


There are 2 instances, each with 6 possible outcomes. Therfore, there are 6*6=36 different permutations of dice rolls. Now, we must find how many of those permutations of dice rols add up to 6, and then divide that by 36, and then multiply by 100 to find the probability. 


Listing:


1. 1+5
2. 2+4
3. 4+2
4. 5+1
5. 3+3


That makes 5. 


Final fraction: 5/36


Probability: 5/36 * 100 = 13.888%


## Problem 3: You roll two fair six-sided dice. What is the probability that the sum at is at least 10?


Again, from the previous problem, there are 36 permutations. 


But wait. We can immedietly "eliminate" certain numbers from the dice. For example, if we roll a 3, its impossible to sum up to 10. Therfore, from both dice, we can eliminate the numbers 1-3 for our convenience. 


Listing: 


1. 4+6
2. 5+5
3. 5+6
4. 6+4
5. 6+5
6. 6+6


This means 6/36, 1/6 * 100 = 16.6666% probability. 


## Problem 4: A bag has 3 red balls and 2 blue balls. You draw 2 balls without replacement. What is the probability both are red?


First draw total balls: 5


First draw red balls: 3


First draw probability: 3/5


Second draw total balls: 4


Second draw red balls: 2


Second draw proabbility: 2/4


Total Probability: 3/5 * 2/4 = 6/20 = 3/10 = 30%


## Problem 5: A standard deck has 52 cards. What is the probability that one drawn card is a heart or a king?


There is an equal chance of every suit: 1/4.


Multiply that chance across all 52 cards, and you get 13 cards. There are 4 kings. 13 + 4 = 17.


But wait. There is a king of hearts that we double counted. Subtract 1. 


So the chance is 16/52 = 4/13 = 30.769%







