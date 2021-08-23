"""Lecture 5 DTN
This is a new fun thing of happiness.
"""


def main():
    """Lecture 5 demo on lists in functions."""
    names = ["Alice", "Bob", "Carly", "David", "Lindsay"]
    ages = [3, 20, 7, 1, 21]
    print(determine_oldest(names, ages))


def determine_oldest(names, ages):
    """Determine the oldest name based on parallel lists."""
    oldest_age = max(ages)
    index = ages.index(oldest_age)
    return names[index]


if __name__ == '__main__':
    main()
