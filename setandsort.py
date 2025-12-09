n = list(map(int, input("Enter numbers separated by spaces: ").split()))
new_Unique=list(set(n))
sorted_list = sorted(new_Unique)
print(f"Sorted unique elements:{sorted_list}")  
# Example Input: 4 2 5 2 3 4 1
# for finding second largest element
#print(f"Second largest element is: {sorted_list[-2]}")

