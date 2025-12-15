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
