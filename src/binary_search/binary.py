class BinarySearch:
    """Binary search algorithm implementation."""

    def __init__(self, arr):
        """Constructor for BinarySearch

        :param arr: List of elements to search in
        :type arr: List[int]
        """
        self.arr = arr

    def iterative(self, target):
        """Iterative binary search algorithm.

        Iterative binary search algorithm to search for an element in a list. It works by dividing the list into two
        halves and comparing the middle element with the target element. If the middle element is equal to the target
        element, the index of the middle element is returned. If the middle element is less than the target element, the
        left half of the list is discarded and the search continues in the right half. If the middle element is greater
        than the target element, the right half of the list is discarded and the search continues in the left half. This
        process is repeated until the target element is found or the list is empty.

        Time complexity: O(log n)

        :param target: Element to search for
        :type target: int
        :return: Index of the target element in the list
        :rtype: int
        """
        left = 0
        right = len(self.arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
