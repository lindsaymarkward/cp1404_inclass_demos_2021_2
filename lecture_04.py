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

# make names title case
names = ["Bob", 'jimbo', 'saLLy']
for name in names:
    name = name.title()
for i in range(len(names)):
    names[i] = names[i].title()
print(names)
names2 = []
for name in names:
    names2.append(name.title())
print(names2)
