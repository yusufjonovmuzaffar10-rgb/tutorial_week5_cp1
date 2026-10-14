# problem 1
# colors = ['red', 'blue', 'black', 'green', 'yellow']
# print(f"The first color: {colors[0]}")
# print(f"The last color: {colors[4]}")
# print(len(colors))

# problem 2
# playlist = ["morning", "journey", "evening"]
# playlist.remove("journey")
# playlist.append("home")
# playlist[1]= "home"
# print(playlist)

# problem 3
# queue = ["Aziza", "Bekzod"]
# queue.append("Malika")
# print(f"Entered:{queue.pop(0)}")
# print(f"Remaining queue:{queue}")


#problem 4
# languages = ["uzbek", "english", "russian"]
# l = input("Enter the language: ").lower()
# if l in list(languages):
#     print("Available")
# else:
#     print("Not available")


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
 