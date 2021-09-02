"""Shift encrypt names/strings from text file
Let string A be the first 6 characters of your last-name
(if your last-name is less than 6 characters,
repeat the last letter until you get a six-character string).

(a) Encrypt string A using ROT3 cipher in the English alphabet.
(b) Encrypt string A using One-Time-Pad cipher,
where the key is 'SECRET'.
"""

from string import ascii_lowercase

NAME_LENGTH = 6
SHIFT_DISTANCE = 3
INPUT_FILENAME = "cp3404_names.txt"
OUTPUT_FILENAME = "cp3404_cryptograms.txt"


def main():
    """Get names and encrypt them."""
    names = get_names(INPUT_FILENAME)
    name_to_cryptogram = encrypt_names(names)
    save_results(name_to_cryptogram, OUTPUT_FILENAME)


def encrypt_names(names):
    name_to_cryptogram = {}
    for name in names:
        cryptogram = encrypt_name(name, SHIFT_DISTANCE)
        name_to_cryptogram[name] = cryptogram
    return name_to_cryptogram


def get_names(filename):
    """Retrieve and process names from text file using minimum length and repeated characters to fill."""
    names = []
    with open(filename) as input_file:
        lines = input_file.readlines()
    for line in lines:
        name = line.strip().lower().replace(' ', '').replace('-', '')  # ward
        names.append(f"{name[:6]:{name[-1]}<6}")  # warddd
    return names


def encrypt_name(name, distance):
    """Use shift to encrypt one name."""
    cryptogram = ""
    number_of_letters_in_alphabet = len(ascii_lowercase)
    for letter in name:
        index = ascii_lowercase.index(letter)
        new_index = (index + distance) % number_of_letters_in_alphabet
        cryptogram += ascii_lowercase[new_index]
    return cryptogram


def save_results(name_to_cryptogram, filename):
    with open(filename, 'w') as output_file:
        for name, cryptogram in name_to_cryptogram.items():
            print(f"{name} => {cryptogram}", file=output_file)


main()
