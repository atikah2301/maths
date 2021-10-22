# Kasiski's Method for finding the keyword length of a Vigenere cipher#

# (1) Find the most frequent trigrams and digrams
# (2) For the most common ones, take note of their positions in the CT
# (3) Calculate the pairwise differences between the position values
# (4) Calculate the pairwise GCDs for the differences
# (5) Calculate the frequencies of each GCD
# (6) The most common GCD will likely be the keyword length

# Assume steps (1) and (2) are done

from collections import Counter
from tabulate import tabulate

def gcd(a, b):
  while b!=0:
    a, b = b, a % b
  return a

def kasiski_method(pos_values=None):
    if not pos_values:
        input_raw = input("Enter position values: ")
        input_strings = input_raw.split(",")
        input_ints = [int(element) for element in input_strings]
        pos_values = input_ints

    # Step (3)
    diffs_list = []
    for i in range(len(pos_values)):
        for j in range(len(pos_values)-1,i,-1):
            diffs_list.append(abs(pos_values[j]-pos_values[i]))
    #print(diffs_list)
    
    # Step (4)
    gcds_list = []
    for i in range(len(diffs_list)):
        for j in range(len(diffs_list)-1,i,-1):
            gcds_list.append(gcd(diffs_list[j],diffs_list[i]))
    #print(gcds_list)

    # Step (5)
    gcd_counter = Counter(gcds_list)
    significant_gcds = []
    counter_sorted_by_value = sorted(gcd_counter.items(), key=lambda x: x[1], reverse=True)
    for key, value in counter_sorted_by_value:
        if value > 1:
            significant_gcds.append((key, value))
    #print(counter_sorted_by_value)

    # Display results as table
    all_gcds = [key for key, value in significant_gcds]
    all_gcds.insert(0,"GCDs")
    all_frequencies = [value for key, value in significant_gcds]
    all_frequencies.insert(0,"Frequency")
    table = tabulate([all_gcds, all_frequencies])
    print(table)


kasiski_method(pos_values=[1,15,89,201,289,320])
#kasiski_method()