def print_invoice(item, price, quantity, currency):
    print("---Invoice---")
    print(f"Item:   {item}")
    print(f"Price:  {price} {currency}")
    print(f"Quantity:  {quantity}")
    print(f"Total:   {quantity*price}  {currency}")

item = input("enter item name: ")
price = float(input("enter price: "))
quantity = int(input("enter quantity:"))
currency = input("enter the currency code:")



print_invoice(item, price, quantity, currency)
