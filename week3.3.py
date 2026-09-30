def minimum(a,b):
    if a>b:
        return b
    else:
        return a

x = float(input("Enter the first number:"))
y = float(input("Enter the second number:"))
m = minimum(x,y)
print(f"the minimum value of {x} and {y} is {m}")