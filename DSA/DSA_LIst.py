# list operations
lst = [1, 2, 3, 4, 5]
lst.append(6)     # Add 6 to the end
lst.remove(3)     # Remove the first occurrence of 3
lst.insert(1, 10) # Insert 10 at index 1
lst.pop()         # Remove the last element (6)
print(lst)        # Output: [1, 10, 2, 4, 5]

# Reverse the list
reversed_lst = lst[::-1]
print(reversed_lst) # Output: [5, 4, 2, 10, 1]

# Convert to a set to get unique elements
n = set(lst)
print(n)          # Output: {1, 2, 4, 5, 10}

# Sort the list in descending order
n1 = sorted(lst, reverse=True)
print(n1)         # Output: [10, 5, 4, 2, 1]

print(max(n1))  # Output: 10
print(min(n1))  # Output: 1
print(len(n1))  # Output: 5