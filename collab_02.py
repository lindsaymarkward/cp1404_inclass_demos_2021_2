
file_in = open("guitars.txt", "r")
for line in file_in:
    line = line.strip()
    print(repr(line))


# result = file_in.readline().strip()
# print(repr(result))
# text = file_in.read()
# print(repr(text))
# print()
# print(text)
file_in.close()
