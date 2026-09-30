def celsius_to_fahrenheit (celsius):
    return round(celsius * 9/5 + 32, 1)
c = float(input("Enter the temperature in Celsiuc:"))
f = celsius_to_fahrenheit(c)
print(f"{c} degrees in Celsiuc equals: {f} degrees in fahrenheit")