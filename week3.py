def rectangle(length,width):
    return length * width
length =  int(input("Please enter the value of length:"))
width = int(input("Please enter the value of width:"))
area1 = rectangle(length, width) # type: ignore
print(f"Area of a rectangle with sides 10 and 15: {area1}")

area2 = rectangle(length*2,width*2)
print(f"Area of a rectengle with sides {length*2} and {width*2}:")
