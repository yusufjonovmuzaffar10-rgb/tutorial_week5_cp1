
#problem 5
n = int(input("Enter the number of days: "))
day=[]
for i in range(n):
    height = int(input())
    day.append(height)
    print(f"Day {i +1}: {height} cm")
    
print(f"Fierst day{day[0]} cm")
print(f"last day{day[n-1]} cm")
print(f"Changes {day[n-1] - day[0]}cm")