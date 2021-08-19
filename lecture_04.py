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

# Strings in a list
# make names title case
names = ["Bob", 'jimbo', 'saLLy']
print(names)

# Why doesn't this work?
for name in names:
    name = name.title()
print(names)

# But this does?
for i in range(len(names)):
    names[i] = names[i].title()
print(names)

# enumerate is good when we need both the index and the element
for i, name in enumerate(names):
    names[i] = name.title()
print(names)

# Let's make a new list
new_names = []
for name in names:
    new_names.append(name.title())
print(new_names)

# Or we could achieve the same in one line with a list comprehension :)
new_names = [name.title() for name in names]

# We could use a list comprehension to make other things, like the lengths of the names
lengths = [len(name) for name in names]
