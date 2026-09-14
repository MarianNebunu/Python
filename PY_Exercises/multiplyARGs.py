def multiply(*args, operator):
    #print(f"Multiplying {args}")
    total_multiply = 1
    total_add = 0
    
    for arg in args:
        if operator == "*":
            total_multiply *= arg
        if operator == "+":
            total_add += arg
    if total_multiply != 1:
        return total_multiply
    else:
        return total_add
        
print(f"Maximum of elements in multyply are: {multiply(2, 3, 4, operator='*')}, {multiply(2, 3, 4, operator='+') }")