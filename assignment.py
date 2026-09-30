number_pots = input("Enter amount of pots:")
is_student = input("Is the customer student (yes/no)?")
money = input("Enter amount of money:")

number_pots=int(number_pots)
money=int(money)

# determine the price per pot
if is_student == "yes" and number_pots >= 5:
    price_per_pot = 6
elif is_student == "yes" and number_pots < 5:
    price_per_pot = 9
elif is_student == "no" and number_pots >= 5:
    price_per_pot = 9
else:
    is_student == "no" and number_pots < 5
    price_per_pot = 12
# calculate the price per pot
total_cost = price_per_pot * number_pots

print(f"Price oer pot: {price_per_pot}$")
print(f"Total cost: {total_cost}$")

#chek the customer budget
if money>total_cost:
    left_money = money - total_cost
    print(f"Money left: {left_money}$")
elif money == total_cost:
    print("Exactly enough money!")
else:
    need_money = total_cost - money
    print(f"More money needed: {need_money}$")