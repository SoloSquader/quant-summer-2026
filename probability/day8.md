# Day 8 Probability

## Overview

Completed Day 8 probability practice.

Focus:

* binomial probability
* dice-roll probability
* card-counting with overlap
* Bayes/update problems
* expected value after new information
* fair value and expected profit

Theme: probability → updated belief → fair value → decision.

## Problem 1

Question: A fair coin is flipped 12 times. What is the probability of getting exactly 7 heads?

Answer: 19.336%

Result: Correct.

## Problem 2

Question: A fair six-sided die is rolled 9 times. What is the probability of getting exactly three rolls that are either 5 or 6?

Initial issue: I accidentally multiplied by an extra arrangement factor after already using combinations.

Correct setup:

C(9, 3) × (1/3)^3 × (2/3)^6

Correct answer: about 27.31%

Result: Incorrect at first, corrected after review.

## Problem 3

Question: A 5-card hand is drawn from a standard 52-card deck. What is the probability that the hand contains exactly 2 kings and exactly 1 heart?

Initial answer: 1.89%

Correct answer: about 1.697%

Result: Incorrect.

Main concept: the king of hearts creates overlap because it is both a king and a heart.

Correct approach requires splitting into cases:

Case 1: king of hearts is included.

Case 2: king of hearts is not included.

This was the hardest problem in the set because it required overlap casework.

## Problem 4

Question: A trader’s signal says “buy” or “sell.” On good days, the signal says “buy” 85% of the time. On bad days, the signal says “buy” 20% of the time. Assume 35% of days are good and 65% are bad. If the signal says “buy,” what is the probability the day is good?

Answer: about 69.2%

Correct answer: about 69.6%

Result: Essentially correct, slight arithmetic/rounding difference.

## Problem 5

Question: A stock is either in a strong regime or weak regime. There is a 30% chance it is in a strong regime. If it is strong, it goes up tomorrow with probability 70%. If it is weak, it goes up tomorrow with probability 40%. What is the overall probability the stock goes up tomorrow?

Answer: 49%

Result: Correct.

## Problem 6

Question: Same situation as Problem 5. Given that the stock went up tomorrow, what is the probability it was in the strong regime?

Answer: 42.852%

Correct answer: about 42.857%

Result: Correct.

## Problem 7

Question: A contract pays $100 if an event happens and $0 otherwise. Before seeing any signal, the event has a 45% chance of happening. A signal says “yes.” The signal says “yes” 80% of the time when the event happens and 30% of the time when the event does not happen. After seeing the “yes” signal, what is the fair value of the contract?

Answer: $68.57

Result: Correct.

Main concept: fair value means expected payout after updating the probability using the signal.

## Problem 8

Question: You can buy the contract from Problem 7 for $58. Using the fair value from Problem 7, what is the expected profit from buying it?

Answer: $10.57

Result: Correct.

## Summary

Completed Day 8 probability.

Main wins:

* Correctly handled Bayes/update problems.
* Correctly connected updated probability to fair value.
* Correctly calculated expected profit after signal information.

Main mistakes:

* Added an extra multiplier in a binomial dice problem.
* Struggled with the card overlap problem involving the king of hearts.

Key lesson:
Bayes and expected value are becoming more intuitive, but card/combinatorics problems still require more careful sample-space discipline and overlap casework.
