
try:
    file_input = open("guitars.txt")
    for line in file_input:
        line = line.strip()
        print(line)
        print('-')
    file_input.close()
except:
    print("Error :(")
