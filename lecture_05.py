"""Lecture 5 DTN
This is a new fun thing of happiness.
"""


def main():
    names = ["Alice", "Bob", "Carly", "David", "Lindsay"]
    ages = [3, 20, 7, 1, 21]
    print(determine_oldest(names, ages))


def determine_oldest(names, ages):
    return names[ages.index(max(ages))]


if __name__ == '__main__':
    main()
