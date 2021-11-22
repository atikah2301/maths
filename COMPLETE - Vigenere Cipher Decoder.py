## Implementation of Kasiski's Method for decoding a Vigenere cipher ##

# This program will automate the following steps, except where stated otherwise:

# (1) Find the most frequent trigrams and digrams
# (2) For the most common ones, take note of their positions in the CT
# (3) Calculate the pairwise differences between the position values
# (4) Calculate the pairwise GCDs for the differences
# (5) Calculate the frequencies of each GCD
# (6) The most common GCD will likely be the keyword length (done manually)
# (7) Extract the caesar shift ciphertexts based on keyword length guess
# (8) Calculate the Chi Squared stat for each possible shift for each substring
# (9) Choose the smallest Chi Squared stats, and determine the keys
# (10) Decrypt and recombine the caesar shift texts to get the Vigenere plaintext


from collections import Counter
from tabulate import tabulate
from math import ceil as round_up

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def get_ngrams(text: int, n=1) -> list[str]:
    # Step (1) - to find digrams and trigrams
    # Step (8) - to help find letter frequencies
    for i in range(len(text)):
        yield text[i: i + n]


