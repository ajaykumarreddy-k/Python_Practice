'''n = [1,2,3,4,5,6,7,8,9,10]
for i in n:
    if( i == 7):
        print("Found 7")
    else:
        print("Not Found 7")
        print(i)'''

# linear search in python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if target is found
    return -1  # Return -1 if target is not found
print(linear_search([1,2,33,4,5,65,43,23,23,2,7], 7))  # Output: 6
#time complexity: O(1) - when item is in the first position
#time complexity: O(n) - when item is in the last position or not present
#space complexity: O(1) - no additional space used

# Example usage of linear search
# binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Initialize the left and right pointers

    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:
            return mid  # Return the index if target is found
        elif arr[mid] < target:
            left = mid + 1  # Move the left pointer to the right
        else:
            right = mid - 1  # Move the right pointer to the left
    return -1  # Return -1 if target is not found
arr_for_binary_search = [1,2,3,423,23,2,3,23,23,23,7]
arr_for_binary_search.sort()
print(binary_search(arr_for_binary_search, 7))


# Bubble Sort
my_list = [64, 34, 25, 12, 22, 11, 90]
n = len(my_list)
for i in range(n):
    for j in range(0, n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]  # Swap if the element found is greater
print("Sorted array is:", my_list)  # Output: Sorted array is: [11, 12, 22, 25, 34, 64, 90]
#time complexity: O(n^2) - for worst case
#space complexity: O(1) - no additional space used
sorted_array1 = sorted(my_list)  # Using built-in sort function
print(sorted_array1)  # Output: [11, 12, 22, 25, 34, 64, 90]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted
        j = i - 1  # Index of the previous element
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place the key at its correct position
    return arr
arr = [5,7,90,1,3,6]
print("insertion sort:", insertion_sort(arr))  # Output: [1, 3, 5, 6, 7, 90]

# Merge Sort
def merge_sort(arr):
    # Base case: if the array has 0 or 1 element, it's already sorted
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
        # Divide the array elements into two halves
        L = arr[:mid]  # Left half
        R = arr[mid:]  # Right half

        # Recursively sort the first half
        merge_sort(L)
        # Recursively sort the second half
        merge_sort(R)

        # Initialize pointers for merging
        i = j = k = 0  # i for left half, j for right half, k for merged array

        # Merge the two sorted halves back into the original array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr
arr_for_merge_sort = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sort:", merge_sort(arr_for_merge_sort))

# Quick Sort
# 2 types of quick sort
# min heap and max heap
# we use pivot and sort and again sort the left and right side of the pivot goes on until sorted
# @ Radix sort - sorts values according to their digit places like 1s, 10s, 100s, etc.
# @ Counting sort - counts the number of occurrences of each element and sorts them based on that count
# we r taking num of reputations present in the array and then sorting them based on that count

# Quick Sort
def quick_sort(arr):
    # Base case: A list with zero or one element is already sorted.
    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot element. Here, we take the middle element.
        pivot = arr[len(arr) // 2]
        
        # Partition the array into three sub-arrays:
        # 1. Elements less than the pivot
        left = [x for x in arr if x < pivot]
        # 2. Elements equal to the pivot
        middle = [x for x in arr if x == pivot]
        # 3. Elements greater than the pivot
        right = [x for x in arr if x > pivot]
        
        # Recursively apply quick_sort to the left and right sub-arrays
        # and combine the results.
        return quick_sort(left) + middle + quick_sort(right)

arr3 = [3,6,8,10,1,2,1]
print("Quick Sort:", quick_sort(arr3))  # Output: [1, 1, 2, 3, 6, 8, 10]
#time complexity: O(n log n) on average worst case: O(n^2)
#space complexity: O(log n) due to recursive stack space

#Counting Sort
def counting_sort(arr):
    # Find the maximum value in the array to determine the range of counts
    max_val = max(arr)
    # Initialize the count array with zeros
    count = [0] * (max_val + 1)
    
    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1
    
    # Reconstruct the sorted array based on the counts
    sorted_index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[sorted_index] = i
            sorted_index += 1
            count[i] -= 1
    
    return arr
arr_for_counting_sort = [4, 2, 2, 8, 3, 3, 1]
print("Counting Sort:", counting_sort(arr_for_counting_sort))  # Output: [1, 2, 2, 3, 3, 4, 8]
#time complexity: O(n + k) where n is number of elements and k is range of input
#space complexity: O(k) for the count array

# Radix Sort
def counting_sort_for_radix(arr, exp):
    max_val = max(arr)
    count = [0] * (max_val + 1) 
    for num in arr:
        count[num] += 1
        index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1
    return arr  
arr_for_radix_sort = [170, 45, 75, 90, 802, 24, 2, 66]
print("Radix Sort:", counting_sort_for_radix(arr_for_radix_sort, 1))  # Output: [2, 24, 45, 66, 75, 90, 170, 802]
#time complexity: O(d*(n + k)) where d is number of digits, n is number of elements and k is range of input
#space complexity: O(k) for the count array     
