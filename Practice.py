print("hello world") # just a print smt
a = 5 # assognment 
b = 10
a,b = b,a # swaped
print("a =", a)
print("b =", b)
# string reversal
s = "Hello"
reversed_string = s[::-1]
print(f"General string is {s}")
print(f"reversed_string:{reversed_string}")
Last_before_element = s[::-1]
print(f"reversed sting {Last_before_element}")
# crating a list 
a_list = [1,2,3,4,5]
reversed_list = a_list[::-1]
print(f"General list is {a_list}")
print(f"Reversed list is {reversed_list}")
# printing a perticular number according to the index
# index starts from 0
a_list[0]
print(f"First element of the list is {a_list[0]}")
#patterns 
n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

#functions 
def sum_of_numbers(x, y):
    return x + y
result = sum_of_numbers(3, 7)
print(f"Sum of numbers is {result}")


    # main practice ends for today and start a new thing tomorrow
    # probabaly lets see may be leet code i will add a new file for that leetcode.py
    # so check that for feature reference i hope so 



    