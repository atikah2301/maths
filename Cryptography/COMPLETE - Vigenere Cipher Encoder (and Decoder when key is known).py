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

def vigenre_encoder(text: str, keyword: str) -> str:
    """Encodes the plaintext by applying shifts to the letters based on the key. Returns ciphertext."""
    plaintext = text.lower().replace(" ","").replace(".","").replace(",","")
    full_keyword = extend_keyword(keyword, len(plaintext))
    key = convert_text_to_indices(full_keyword)
    num_plaintext = convert_text_to_indices(plaintext)

    num_ciphertext = []
    for i in range(len(plaintext)):
        num_ciphertext.append((num_plaintext[i] + key[i]) % 26)

    ciphertext = convert_indices_to_text(num_ciphertext)
    return ciphertext.upper()

def vigenre_decoder(ciphertext: str, keyword: str) -> str:
    """Encodes the plaintext by applying shifts to the letters based on the key. Returns ciphertext."""
    full_keyword = extend_keyword(keyword, len(ciphertext))
    key = convert_text_to_indices(full_keyword)
    num_ciphertext = convert_text_to_indices(ciphertext)

    num_plaintext = []
    for i in range(len(ciphertext)):
        num_plaintext.append((num_ciphertext[i] - key[i]) % 26)

    plaintext = convert_indices_to_text(num_plaintext)
    return plaintext

print(vigenre_encoder("hello My Name is Atikah..,", "hi"))
print(vigenre_decoder("OMSTVUFVHULQZIAQRIO", "hi"))