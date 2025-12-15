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
