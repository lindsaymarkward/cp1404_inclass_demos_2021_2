"""
DTN - count letters in name
"""
VOWELS = "aeiou"
number_of_vowels = 0
name = "Bobby McAardvark"
for character in name:
    if character.lower() in VOWELS:
        number_of_vowels += 1
print(f"Out of {len(name)} letters, {name} has {number_of_vowels} vowels")
