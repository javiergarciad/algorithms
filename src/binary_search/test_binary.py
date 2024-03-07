import pytest
from binary import BinarySearch


# Test cases for BinarySearch class
class TestBinarySearch:
    def test_iterative_search(self):
        # Test case 1: Target element exists in the list
        arr = [1, 2, 3, 4, 5]
        bs = BinarySearch(arr)
        assert bs.iterative(3) == 2

        # Test case 2: Target element does not exist in the list
        arr = [1, 2, 3, 4, 5]
        bs = BinarySearch(arr)
        assert bs.iterative(6) == -1

        # Test case 3: Empty list
        arr = []
        bs = BinarySearch(arr)
        assert bs.iterative(1) == -1

        # Test case 4: Single element list
        arr = [5]
        bs = BinarySearch(arr)
        assert bs.iterative(5) == 0

        # Test case 5: Target element is the first element in the list
        arr = [1, 2, 3, 4, 5]
        bs = BinarySearch(arr)
        assert bs.iterative(1) == 0

        # Test case 6: Target element is the last element in the list
        arr = [1, 2, 3, 4, 5]
        bs = BinarySearch(arr)
        assert bs.iterative(5) == 4

        # Test case 7: Target element is greater than all elements in the list
        arr = [1, 2, 3, 4, 5]
        bs = BinarySearch(arr)
        assert bs.iterative(10) == -1

        # Test case 8: Target element is smaller than all elements in the list
        arr = [1, 2, 3, 4, 5]
        bs = BinarySearch(arr)
        assert bs.iterative(0) == -1

        # Test case 9: Target element is between two elements in the list
        arr = [1, 2, 3, 4, 5]
        bs = BinarySearch(arr)
        assert bs.iterative(2.5) == -1


# Run the tests
if __name__ == "__main__":
    pytest.main()
