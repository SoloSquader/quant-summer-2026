# Problem 1: Prove by induction that: 1 + 2 + 3 + ... + n = n(n + 1)/2 for all positive integers n.


P(n): 1 + 2 + 3 + ... + n = n(n + 1)/2


Base case: P(1)


P(1): 1 = 1(1+1)/2


-> 1 = 1(2)/2


-> 1 = 1


The base case is proven true.


Now, replace n with k and assume P(k) is true for any k:


P(k): 1 + 2 + 3 ... + k = k(k+1)/2


Now, replace k with k+1 and attempt to prove it true:


P(k + 1): 1 + 2 + 3 ... + k + k + 1 = k(k+1)/2 + k + 1


P(k + 1): 1 + 2 + 3 ... + k + k + 1 = k(k+1)/2 + 2(k + 1)/2


P(k + 1): 1 + 2 + 3 ... + k + k + 1 = (k+1)(k+2)/2


Therefore, if P(k) is true, P(k+1) is true. Since P(1) is true, the statement is true for all positive integers n by induction. 



# Problem 2: Prove by induction that: 1 + 3 + 5 + ... + (2n − 1) = n² for all positive integers n.


P(n) = 1 + 3 + 5 + ... + (2n − 1) = n²


Proving the base case true:


P(1): 1 = (1)^2


-> P(1): 1 = 1


The base case is proven to be true. Now, lets replace the n in P(n) with k, creating P(k), and assuming it true for all k that are integers. 


P(k): 1 + 3 + 5 + ... + (2k − 1) = k²


Now, replace k with (k + 1) and attempt to prove it true.


P(k+1): 1 + 3 + 5 + ... + (2k - 1) + (2k + 1) = k^2 + (2k + 1)


-> P(k+1): 1 + 3 + 5 + ... + (2k - 1) + (2k + 1) = (k + 1)^2


Therefore, if P(k) is true, then P(k + 1) is also true. Since P(1) is true, the statement P(n) is true for all integers n by induction. 


# Problem 3: Prove by induction that: 2 + 4 + 6 + ... + 2n = n(n + 1) for all positive integers n.


P(n): 2 + 4 + 6 + ... + 2n = n(n + 1)


Prove a base case true using P(1):


P(1): 2 = 1(1+1)


-> P(1): 2 = 2


The base case is now proven to be true. 


Now, replace n with k in P(n), creating P(k), and assume it to be true for all positive integers:


P(k): 2 + 4 + 6 + ... + 2k = k(k + 1)


Now, replace k with k + 1 and try to prove it true. 


P(k + 1): 2 + 4 + 6 + ... + 2k + 2(k + 1) = k(k + 1) + 2(k + 1)


-> P(k + 1): 2 + 4 + 6 + ... + 2k + 2(k + 1) = (k + 1)(k + 2)


P(k + 1) has been proven true. 


Therefore, if P(k) is true, P(k + 1) must also be true. Since P(1) is true, P(n) must also be true for all positive integers by induction. 


# Problem 4: Prove by induction that: 2ⁿ ≥ n + 1 for all positive integers n.

P(n): 2ⁿ ≥ n + 1


Check and see if a base case is true using P(1):


P(1): 2 >= 1 + 1


-> P(1): 2 >= 2


The base case has been proven to be true. 


Now, replace n with k in P(n) to make P(k), and assume it to be true for all positive integers:


P(k): 2^k ≥ k + 1


Now, replace k with k + 1 in P(k) and try to prove it true. 


P(k + 1):  2^(k + 1) >= k + 2


2^k ≥ k + 1


2^(k + 1) >= 2k + 2


2k + 2 > k + 2 for all intergers k. Therefore, 

P(k+1) must be true is P(n) is true. Since P(1) is true, P(n) must be true for all integers n by induction. 



# Problem 5: Prove by induction that: 3 + 6 + 9 + ... + 3n = 3n(n + 1)/2 for all positive integers n.


P(n): 3 + 6 + 9 + ... + 3n = 3n(n + 1)/2


Prove a base case true: P(1)


P(1): 3 = 3(1)(1+1)/2


-> P(1): 3 = 3


The base case is now proven true.


Now, replace n with k to create P(k), and assume P(k) is true for all integers k. 


P(k): 3 + 6 + 9 + ... + 3k = 3k(k + 1)/2


Now, try to prove P(k+1) is true:


P(k + 1): 3 + 6 + 9 + ... + 3k + 3(k + 1) = 3k(k + 1)/2 + 3(k + 1)


-> P(k + 1): 3 + 6 + 9 + ... + 3k + 3(k + 1) = 3k(k + 1)/2 + 6(k + 1)/2


-> P(k + 1): 3 + 6 + 9 + ... + 3k + 3(k + 1) = ( 3k(k + 1) + 6(k + 1) )/2


-> P(k + 1): 3 + 6 + 9 + ... + 3k + 3(k + 1) = ((k + 1)(3k + 6))/2


Plug in "k + 1" into the original equation: 3(k + 1)((k + 1) + 1)/2


Set the two equations equal to each other to prove equality:


3(k + 1)((k + 1) + 1)/2 = ((k + 1)(3k + 6))/2


-> 3(k + 1)((k + 1) + 1) = ((k + 1)(3k + 6))


-> 3(k + 1)(k + 2) = (k + 1)(3k + 6)


-> 3(k + 2) = 3k + 6


-> k + 2 = k + 2


-> k = k


Therefore, if P(k) is true for all positive integers k, P(k + 1) must also be true for all positive integers k.


Since P(1) is true, P(n) must also be true for all positive integers n by induction. 












