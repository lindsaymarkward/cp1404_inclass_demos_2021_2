"""
DTN - files

file_input = open file "switch.txt" for reading
contents = read file_input
close file_input

if contents == "on"
    new_contents = "off"
else
    new_contents = "on"

file_output = open file "switch.txt" for writing
write new_contents to file_output
close file_output
"""

# name = "Bob"
# age = 37
# print(f"{name.title()} is {age}.")
# print(f"{name},{age}", file=)

file_input = open("switch.txt", "r")
contents = file_input.read()
file_input.close()
if contents == "on":
    new_contents = "off"
else:
    new_contents = "on"
file_output = open("switch.txt", "w")
print(new_contents, file=file_output, end="")
file_output.close()
