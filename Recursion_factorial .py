def factorial(n):
    if n==0 or n==1:
        return  1
    else:
        return n*factorial(n-1)
n = int(input("enter a value: "))
print(factorial(n))  # in vs code it runs in general but in the vs u have to pass the value thats it
# for a defing the function
def add(a,b):
    print a+b
result = add(5,7)
print(result)