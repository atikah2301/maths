# Kasiski's Method for finding the keyword length of a Vigenere cipher#

# (1) Find the most frequent trigrams and digrams
# (2) For the most common ones, take note of their positions in the CT
# (3) Calculate the pairwise differences between the position values
# (4) Calculate the pairwise GCDs for the differences
# (5) Calculate the frequencies of each GCD
# (6) The most common GCD will likely be the keyword length

def kasiski_method(pos_values=None):
    if not pos_values:
        input_raw = input("Enter position values: ")
        input_strings = input_raw.split(",")
        input_ints = [int(element) for element in input_strings]
        pos_values = input_ints
kasiski_method(pos_values=[1,15,89,201,289,320])
#kasiski_method()