"""CP1404 lecture 03"""
from string import ascii_letters


def main():
    """Demonstrate line functions."""
    length_of_line = int(input("How many? "))
    print_line(length_of_line)
    print_line(20)
    print_line(100)


def print_line(length):
    """Print a line of length hyphens."""
    print(length * '-')


def count_letters(string):
    count = 0
    for character in string:
        if character in ascii_letters:
            count += 1
    return count


def test_count():
    assert count_letters("CP1404") == 2
    assert count_letters("1404 a 983") == 1
    print(count_letters("CP1401") > count_letters("CP1404"))


# test_count()

main()

