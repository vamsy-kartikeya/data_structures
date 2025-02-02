class SortingAlgorithms:
    @staticmethod
    def bubble_sort(arr):
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(arr)
        for i in range(n):
            # Flag to optimize if array is already sorted
            swapped = False
            
            # Last i elements are already in place
            for j in range(0, n-i-1):
                # Swap if current element is greater than next
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            
            # If no swapping occurred, array is sorted
            if not swapped:
                break
        return arr

    @staticmethod
    def selection_sort(arr):
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(arr)
        for i in range(n):
            # Find minimum element in unsorted array
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            # Swap found minimum with first element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    @staticmethod
    def insertion_sort(arr):
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            # Move elements greater than key one position ahead
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    @staticmethod
    def binary_search(arr, target):
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        Note: Array must be sorted
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1  # Element not found 