#!/usr/bin/env python3


def import_from_file(filename):
    with open(filename) as f:
        return f.read()


def get_lists(data):
    left = []
    right = []
    for line in data.split("\n"):
        if not line:
            continue
        lft, rght = line.split()
        left.append(int(lft))
        right.append(int(rght))
    return left, right


def main():
    data = import_from_file("data.txt")
    left, right = get_lists(data)

    left.sort()
    right.sort()

    zipped = zip(left, right)

    ttl = 0
    for line in zipped:
        ttl += abs(line[0] - line[1])

    print(ttl)


if __name__ == "__main__":
    main()

# """Calculate the sum of absolute differences between two sorted number columns."""
#
# from pathlib import Path
# from typing import Tuple, List
#
#
# def read_input_file(filepath: str) -> str:
#     """Read and return the contents of the input file.
#
#     Args:
#         filepath: Path to the input file
#
#     Returns:
#         The contents of the file as a string
#     """
#     return Path(filepath).read_text()
#
#
# def parse_number_columns(data: str) -> Tuple[List[int], List[int]]:
#     """Parse input data into two lists of numbers.
#
#     Args:
#         data: String containing newline-separated pairs of numbers
#
#     Returns:
#         Tuple of two lists containing the left and right numbers
#     """
#     # Skip empty lines and split each line into two numbers
#     pairs = [line.split() for line in data.splitlines() if line.strip()]
#     # Unzip the pairs into two lists and convert to integers
#     return tuple(map(lambda x: sorted([int(n) for n in x]), zip(*pairs)))
#
#
# def calculate_total_difference(numbers1: List[int], numbers2: List[int]) -> int:
#     """Calculate the sum of absolute differences between two lists of numbers.
#
#     Args:
#         numbers1: First list of integers
#         numbers2: Second list of integers
#
#     Returns:
#         Sum of absolute differences between corresponding numbers
#     """
#     return sum(abs(n1 - n2) for n1, n2 in zip(numbers1, numbers2))
#
#
# def main() -> None:
#     """Main program entry point."""
#     data = read_input_file("data.txt")
#     left_numbers, right_numbers = parse_number_columns(data)
#     total_difference = calculate_total_difference(left_numbers, right_numbers)
#     print(total_difference)
#
#
# if __name__ == "__main__":
#     main()
