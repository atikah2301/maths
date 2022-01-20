# Calculates T(x), which is x to the power of some e, all mod n
# e.g. if e=2 and n=3 then T(12) = 12^2 mod 3 = 24 mod 3 = 0

# Step 1: Find e as the unique minimal sum of powers of 2
# Step 2: Calculate 2^k for all k up to the maximum power needed from step 1
# Step 3: Calculate x^2^k for all k.. iteratively, by squaring the previous value and reducing mod n
# Step 4: Multiply together the x^2^k values needed to get x^e and reduce mod n


from math import log
from tabulate import tabulate
