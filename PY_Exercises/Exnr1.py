def add (a, b):
    print(f"Adding {a} + {b}")
    return (a + b)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = add(a, b)
print(f"The sum of {a} and {b} is {result}.")