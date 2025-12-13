#Maximum Subarray Problem - U
arr = [-1,0,-3,4,-1,1,2,-3,-5]
'''def find_max_subarray_sum(arr):
    max_sum = float('-inf') # defines the -ve infinity -  inf indicates that
    current_sum = 0

    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum
print(find_max_subarray_sum(arr))  # Output: 6'''
# we can use this thing
'''max_sum = arr[0]
current_sum = arr[0]    
for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)
print(max_sum)  # Output: 6'''
