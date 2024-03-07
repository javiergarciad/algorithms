from binary import BinarySearch


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    binary_search = BinarySearch(arr)
    print(binary_search.iterative(5))  # Output: 4
    print(binary_search.iterative(11))  # Output: -1


if __name__ == "__main__":
    main()
