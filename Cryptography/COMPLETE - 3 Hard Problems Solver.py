# When choosing an encryption algorithm for a public key cryptosystem, your algorithm should be easy to solve one way
# but hard to solve when the problem is reversed.
# The code here should solve 3 such "hard problems" in a cyclic fashion
# Where one problem can be easily solved if the solution to another of the 3 is known.

# Problem 1 - Prime factorisation of n into odd primes p and q
# Problem 2 - Finding Carmichael's lambda value or Euler's phi value of n
# Problem 3 - Finding the inverse of a power map function on power e, reduced mod n
