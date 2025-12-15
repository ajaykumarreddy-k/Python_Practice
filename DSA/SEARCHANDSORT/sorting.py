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
