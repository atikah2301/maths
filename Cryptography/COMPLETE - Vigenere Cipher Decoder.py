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

# Used to retrieve caesar shift lengths from keywords
english_alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Used to calculated expected frequencies for Chi Squared stat
standard_letter_frequencies = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

# Used to map letters to their frequencies
english_letters_and_frequencies = list(zip(english_alphabet, standard_letter_frequencies))


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def get_ngrams(text: int, n=1) -> list[str]:
    # Step (1) - to find digrams and trigrams
    # Step (8) - to help find letter frequencies
    for i in range(len(text)):
        yield text[i: i + n]


def find_positions(ciphertext: str, phrase: str) -> list[int]:
    # Step (2)
    all_indices = []
    index = ciphertext.find(phrase, 0, len(ciphertext) - 1)
    while index != -1:
        all_indices.append(index)
        index = ciphertext.find(phrase, index + len(phrase), len(ciphertext) - 1)
    return all_indices


def tabulate_frequencies(counter: Counter, title: str, threshold=1) -> None:
    # Step (6) is done intuitively by making a guess based on the tabulated results
    # Only tabulate values with a frequency above a given threshold
    counter_sorted_by_value = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    significant_results = []
    for key, value in counter_sorted_by_value:
        if value > threshold:
            significant_results.append((key, value))

    significant_values = [key for key, value in significant_results]
    significant_values.insert(0, title)
    significant_frequencies = [value for key, value in significant_results]
    significant_frequencies.insert(0, "Frequency")
    table = tabulate([significant_values, significant_frequencies])
    print(table)


def find_key_length(pos_values: list[int]) -> None:
    # Step (3)
    diffs_list = []
    for i in range(len(pos_values)):
        for j in range(len(pos_values) - 1, i, -1):
            diffs_list.append(abs(pos_values[j] - pos_values[i]))
    print(diffs_list)

    # Step (4)
    gcds_list = []
    for i in range(len(diffs_list)):
        for j in range(len(diffs_list) - 1, i, -1):
            gcds_list.append(gcd(diffs_list[j], diffs_list[i]))

    # Step (5)
    gcd_counter = Counter(gcds_list)
    tabulate_frequencies(gcd_counter, "GCDs", threshold=4)


def get_caesar_substrings(ciphertext: str, key_length: int) -> list[str]:
    # Step (7)
    ct_length = len(ciphertext)
    caesar_shifts = []
    remainder = ct_length % key_length
    if remainder != 0:
        ciphertext += " " * remainder  # padding for shorter substrings
    number_of_full_substrings = round_up(ct_length / key_length)
    for i in range(key_length):  # for each caesar shift ...
        substring = ""
        for j in range(number_of_full_substrings):  # ... get the ciphertext for that shift
            letter = ciphertext[j * key_length: j * key_length + key_length][i]
            substring += letter
        caesar_shifts.append(substring)
    return caesar_shifts


def apply_caesar_shift(text: str, n: int) -> str:
    shifted_text = ""
    n = n % 26
    for char in text:
        num = english_alphabet.index(char)
        shifted_text += english_alphabet[(num + n) % len(english_alphabet)]
    return shifted_text


def undo_caesar_shift(text: str, n: int) -> str:
    reverse_shift = 26 - n
    return apply_caesar_shift(text, reverse_shift)


def chi_squared(unshifted_freqs: list[str, int], substring_len: int) -> int:
    # Step (8)
    expected_letter_counts = dict([(letter, round(freq * substring_len, 4))
                                   for (letter, freq)
                                   in english_letters_and_frequencies])
    chi_square_sum = 0
    for letter, freq in unshifted_freqs:
        a = freq
        e = expected_letter_counts[letter]
        current_chi_square_value = (a - e) ** 2 / e
        chi_square_sum += current_chi_square_value
    return chi_square_sum


def get_key_letter(substring: str) -> str:
    # Step (9)
    chi_squared_stats = []
    for i in range(0, len(english_alphabet)):
        unshifted_substring = undo_caesar_shift(substring, i)
        letters = get_ngrams(unshifted_substring, n=1)
        letter_frequency = Counter(letters)
        chi_square_val = chi_squared(letter_frequency.items(), len(substring))
        chi_squared_stats.append(chi_square_val)

    chi_squared_pairs = list(zip(english_alphabet, chi_squared_stats))
    chi_squared_pairs.sort(key=lambda x: x[1])
    best_fitting_letter, smallest_chi_square = chi_squared_pairs[0]
    return best_fitting_letter


def get_decryption_key(substrings: list[str]) -> str:
    # Step (9)
    keyword = ""
    for i in range(len(substrings)):
        substrings[i] = substrings[i].strip()
        keyword += get_key_letter(substrings[i])
    return keyword


def get_encryption_key(keyword: str) -> str:
    # Step (9)
    n = len(english_alphabet)
    inverse_keyword = ""
    for char in keyword:
        num = english_alphabet.index(char)
        inverse_letter = english_alphabet[(n - num) % n]
        inverse_keyword += inverse_letter
    return inverse_keyword


def decode_vigenere_ciphertext(substrings: list[str], key: str) -> str:
    # Step (10)
    decrypted_substrings = []
    for i in range(len(key)):
        shift = english_alphabet.index(key[i])
        decrypted_substring = apply_caesar_shift(substrings[i], shift)
        decrypted_substrings.append(decrypted_substring)

    plaintext = ""
    for j in range(len(decrypted_substrings[0])):
        for str in decrypted_substrings:
            if j == len(str):
                continue
            plaintext += str[j]

    return plaintext.lower()


# Run this code to see a table
# of all the most common digrams and trigrams, with their frequencies
with open('cipher_text.txt') as file:
    ciphertext = file.read().replace('\n', '').replace(' ', '')

    digrams = get_ngrams(ciphertext, n=2)
    digram_counter = Counter(digrams)
    # tabulate_frequencies(digram_counter, "Digrams", threshold=6)

    trigrams = get_ngrams(ciphertext, n=3)
    trigram_counter = Counter(trigrams)
    # tabulate_frequencies(trigram_counter, "Trigrams", threshold=2)

# Run this code on different trigrams and digrams until you can guess a keyword length
with open('cipher_text.txt', 'r') as file:
    ciphertext = file.read().replace('\n', '').replace(' ', '')
    ngram = "QL"
    positions = find_positions(ciphertext, ngram)
    print(positions)
    find_key_length(pos_values=positions)

# Run this code to split the ciphertext
# into its constituent caesar shift ciphertexts, based on guessed keyword length
# then find the encryption / decryption keys using chi-squared stats
# finally, retrieve the plaintext through decryption
with open('cipher_text.txt', 'r') as file:
    ciphertext = file.read().replace('\n', '').replace(' ', '')
    key_length = 14
    substrings = get_caesar_substrings(ciphertext, key_length)

    # Tabluate the letter frequencies for each substring
    # for i in range(len(substrings)):
    #     substrings[i] = substrings[i].strip()
    #     letters = get_ngrams(substrings[i], n=1)
    #     letter_frequency = Counter(letters)
    #     tabulate_frequencies(letter_frequency, f"Caesar Shift {i + 1}", threshold=1)

    key = get_decryption_key(substrings)
    print(key)
    inv_key = get_encryption_key(key)
    print(inv_key)

    print(decode_vigenere_ciphertext(substrings, inv_key))

