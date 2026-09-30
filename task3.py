
year = int(input("please enter your year of birth:"))
print("you have entered:", year, type(year))
print("your age:", 2026 - year)

futureyear = int(input("please enter you want year:\n>>>"))
print("you will be", futureyear - year, "years old in the year", futureyear)

# 1-shart
if futureyear <= 2040:
    print(f"you are on your prime age at {futureyear - year}")

# 2-shart (agar 1-shartga tushmasa, shuni tekshiradi)
elif 2040 < futureyear <= 2050:
    # Javobni 'javob' degan o'zgaruvchiga saqlaymiz va int() ni olib tashlaymiz
    javob = input("i think already you have 2 or more children right? (yes/no): ")
    
    # Kiritilgan javobni tekshiramiz
    if javob == "yes":
        print("i know because i am patrick Jane")
    else:
        print("i have doubt with you you are boydoq")
    input("What is your name?")
    print("all right!")
    javob == input("I have any question You say (yes/no)")
    input("Nowadays are you living in Khorezm:\n>>>")
    # Kiritilgan javoblarni tekshiramiz
    if javob == "yes":
         input("Tell me about street, you live:\n>>>")
         print("All right")
    else:
        javob == "no"
        print("ohh nice to meet you good luck")
    