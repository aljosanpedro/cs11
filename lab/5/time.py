HOURS_TO_MINUTES = 60
MINUTES_TO_SECONDS = 60


hours = int(input("Hours: "))
minutes = int(input("Minutes: "))

input_hours, input_minutes = hours, minutes

hours *= HOURS_TO_MINUTES
hours *= MINUTES_TO_SECONDS

minutes *= MINUTES_TO_SECONDS

seconds = hours + minutes

print(f"{input_hours} hours and {input_minutes} minutes is {seconds} seconds.")