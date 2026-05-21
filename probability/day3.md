# Day 3 Probability


## Problem 1


You roll two fair six-sided dice.


Given that the sum is **8**, what is the probability that at least one die shows a 3?


Permutations that add up to 8:


 - 2+6
 - 3+5
 - 4+4
 - 5+3
 - 6+2


Out of those, only 2 have "3" in them. This makes the probability 2/5, or 40%. 

## Problem 2


You flip 5 fair coins.


What is the probability of getting **exactly 3 heads**?


hmmm....wondering if there is a mathematical way to do these types of questions. Probably some permutations formula, but I dont know it yet. 


It seems listing is all I can do. There must be 2^5 different permutations, which is equal to 32. We will represent heads as 1, trails as 0. 

1. 11100
2. 11010
3. 11001
4. 10110
5. 10011
6. 10101
7. 01011
8. 00111
9. 01110
10. 01101


Quite nervous that I didnt list em all...


But fine. 10/32. 31.25%




## Problem 3


A bag has 4 red balls, 3 blue balls, and 3 green balls.


You draw 3 balls without replacement.


What is the probability that all 3 balls are red?


4/10 * 3/9 * 2/8 = 2/5 * 1/3 * 1/4 = 2/60 = 1/30 = 3.33333%


## Problem 4


Same bag: 4 red balls, 3 blue balls, and 3 green balls.


You draw 3 balls without replacement.


What is the probability that you get **exactly 2 red balls**?


This one looks much more tricky. Assume 1 = got red ball. Assume 0 = didnt get red ball. Possibilities that work:


1. 110
2. 011
3. 101


And then I think add up the probability of each one. 


1. 4/10 * 3/9 * 6/8 = 0.1 = 10%
2. 6/10 * 4/9 * 3/8 = 0.1 = 10%
3. 4/10 * 6/9 * 3/8 = 0.1 = 10%


10% + 10% + 10% = 30%


## Problem 5


A number is chosen randomly from 1 through 60.


What is the probability that it is divisible by 3 **or** divisible by 4?


There are 60 numbers total. Multiples of 3:


1. 3
2. 6
3. 9
4. 12
5. 15
6. 18
7. 21
8. 24
9. 27
10. 30
11. 33
12. 36
13. 39
14. 42
15. 45
16. 48
17. 51
18. 54
19. 57
20. 60


Multiples of 4: 


1. 4
2. 8
3. 12 DULPICATE
4. 16
5. 20
6. 24 DULPICATE
7. 28
8. 32
9. 36 DULPICATE
10. 40
11. 44
12. 48 DULPICATE
13. 52 
14. 56
15. 60 DULPICATE


There are 30 numbers. This makes up 50%.




## Problem 6

A game works like this:


You roll one fair six-sided die.


- If you roll a 1, you win $3.
- If you roll a 2, 3, or 4, you win $6.
- If you roll a 5 or 6, you win $0.


What is the expected value of the game?


Each outcome is equally likely. So the answer is the total amount you can win adding up from all outcomes, divided by the amount of outcomes. 


That would give you the average amount per roll. 


Total: 3 + 6 + 6 + 6 + 0 + 0 = 21


Outcomes: 6

Answer: 21/6 = $3.50 


## Problem 7

A game costs **$2** to play.


You roll one fair six-sided die.

- If you roll a 6, you win $10.
- Otherwise, you win $0.

What is the expected profit per play?


Same logic, but you just subtract 2 at the end. It's like shifting the entire graph down by 2.


Total: 10 + 0 + 0 + 0 + 0 + 0


Outcomes: 6

Answer: 10/6 - 2 = $-0.33


## Problem 8

A card is drawn from a standard 52-card deck.

Given that the card is a **face card**: jack, queen, or king, what is the probability that it is a king?

There are 4 jacks, 4 queens, and 4 kings. 

So the probability is 4/12 = 1/3 = 33.33%
