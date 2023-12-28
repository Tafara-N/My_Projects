time = input("Enter time: ")

hour, minutes = time.split(":")
hour = int(hour)
minutes = int(minutes)

if (hour == 7 and (minutes >= 00 and minutes <= 59)) or (hour == 8 and minutes == 00):
    print("Breakfast")
