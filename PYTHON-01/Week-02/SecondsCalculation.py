totalSeconds = int(input("Insert the quantity of seconds do you want converter: "))

hours = totalSeconds // 3600
restTime = totalSeconds % 3600
minutes = restTime // 60
restSeconds = restTime % 60

print(f"Hours: {hours}\nMinutes: {minutes}\nSeconds: {restSeconds}")
