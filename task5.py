year = int(input('Enter the year you were born: '))
age = 2026 - year
if age >= 0 and age < 10:
    print(f'Oh you are just a child, {age} years old child!')

elif age >= 10 and age < 20:
    print(f'You must be a teenager. {age} years old and just like me!')
elif age >= 20 and age < 50:
    print(f'You are {age}. Middle aged man')
elif age >= 50 and age < 100:
    print(f'You are {age} years old. You must be pretty old man. How did the dinasours look like?')
elif age >= 100 and age <= 150:
    print(f"{age}? Isn't it suspicous? Are you a vampire?")
elif age > 150:
    print(f'Common man, You must be dead already! A mortal man can not reach to {age}')
elif age < 0 and age != 2026 - 9430:
    print('Really? You have not even born yet!')
elif age == 2026 - 9430:
    print('BYE!')

else:
    print('You entered an invalid value')