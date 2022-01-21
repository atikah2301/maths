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
