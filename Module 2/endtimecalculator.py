# calculating the end time (00:00) of a period of time

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins = mins + dura  # total time elapsed in minutes
hour = hour + (mins // 60)  # total hours elapsed
mins = mins % 60  # remaining mins elapsed

print(hour, mins, sep=":")  # print in 00:00 format
