from math import lcm

english_alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_indices = [i for i in range(26)]
char_to_int = dict(zip(english_alphabet, alphabet_indices))
int_to_char = dict(zip(alphabet_indices, english_alphabet))

def convert_text_to_indices(text: str) -> list[int]:
    """Converts plaintext to its alphabetic indices"""
    indices = []
    for char in text.upper():
        indices.append(char_to_int[char])
    return indices

def convert_indices_to_text(indices: list[int]) -> str:
    """Converts plaintext to its alphabetic indices"""
    text = ""
    for i in indices:
        text += int_to_char[i]
    return text.lower()

def caesar_shift_single(char: str, shift: int) -> str:
    """Shifts a single letter"""
    start_pos = convert_text_to_indices(char)
    return convert_indices_to_text([start_pos+shift])

def extend_keyword(keyword: str, length: int) -> str:
    """Takes a keyword, and repeats it until a desired length is reached"""
    new_keyword = ""
    full_repeats = length//len(keyword) # number of full repeats
    extra = length % len(keyword)
    for i in range(full_repeats):
        new_keyword += keyword
    new_keyword += keyword[:extra]
    return new_keyword

def vigenre_encoder(text: str, *keywords: str) -> str:
    """Encodes the plaintext by applying shifts to the letters based on the key. Returns ciphertext."""
    if len(keywords) > 1:
        keyword = key_composer(*keywords)
    else:
        keyword = keywords[0]

    plaintext = text.lower().replace(" ","").replace(".","").replace(",","")
    full_keyword = extend_keyword(keyword, len(plaintext))
    key = convert_text_to_indices(full_keyword)
    num_plaintext = convert_text_to_indices(plaintext)

    num_ciphertext = []
    for i in range(len(plaintext)):
        num_ciphertext.append((num_plaintext[i] + key[i]) % 26)

    ciphertext = convert_indices_to_text(num_ciphertext)
    return ciphertext.upper()

def vigenre_decoder(ciphertext: str, *keywords: str) -> str:
    """Encodes the plaintext by applying shifts to the letters based on the key. Returns ciphertext."""
    if len(keywords) > 1:
        keyword = key_composer(*keywords)
    else:
        keyword = keywords[0]

    full_keyword = extend_keyword(keyword, len(ciphertext))
    key = convert_text_to_indices(full_keyword)
    num_ciphertext = convert_text_to_indices(ciphertext)

    num_plaintext = []
    for i in range(len(ciphertext)):
        num_plaintext.append((num_ciphertext[i] - key[i]) % 26)

    plaintext = convert_indices_to_text(num_plaintext)
    return plaintext

# To compose any number of vigenere ciphers, you must compose their keys and apply the new key to the plaintext
# To compose the keys, calculate their LCM (lowest common multiple), and extend each key to this length
# Apply each key successively to the plaintext OR
# Apply each key to each other then to the plaintext

def key_composer(*keywords: str) -> str:
    keys = [convert_text_to_indices(keyword) for keyword in keywords] # get each key as a list of indices
    key_lengths = [len(key) for key in keys] # get the length of each key
    new_key_length = lcm(*key_lengths) # calculate the length of the new key
    long_keys = [extend_keyword(keyword, new_key_length) for keyword in keywords] # make keys the same length
    new_key = long_keys[0] # starting with the first key, encode the keys with each other
    for i in range(len(long_keys)-1):
        new_key = vigenre_encoder(new_key, long_keys[i+1])
    return new_key.lower()

print(vigenre_encoder("hello My Name is Atikah..,", "hi", "hey"))
print(vigenre_decoder("OMSTVUFVHULQZIAQRIO", "hi"))
print(vigenre_decoder("VQQAZSMZFBPOGMYXVGV", "omfplg"))
print(vigenre_decoder("VQQAZSMZFBPOGMYXVGV", "hi", "hey"))
print(key_composer("hi", "hey"))