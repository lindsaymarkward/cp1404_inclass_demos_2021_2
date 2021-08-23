"""Lecture 5 DTN"""


def main():
    names = ["Alice", "Bob", "Carly", "David"]
    ages = [3, 20, 7, 1]
    print(determine_oldest(names, ages))


def determine_oldest(names, ages):
    return names[ages.index(max(ages))]


main()
