def add_time(start: str, add: str, day=None):
    start = start.split(" ")

    start_time = start
    if start_time[1].lower() == "am":
        start_time = start_time[0].split(":")
        start_time = int(start_time[0]) * 60 + int(start_time[1])
    elif start_time[1].lower() == "pm":
        start_time = start_time[0].split(":")
        start_time = (12 + int(start_time[0])) * 60 + int(start_time[1])

    add = add.split(":")
    add = int(add[0]) * 60 + int(add[1])

    result = start_time + add
    d_pass = int(add / 24 / 60)
    d = int(result / 24 / 60)
    h = int((result - d * 24 * 60) / 60)
    m = result - d * 24 * 60 - h * 60

    out = "Returns: "
    ampm = "AM"
    next_daty = False
    hour = h
    week_day = ""

    if day != None:
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day = days.index(day.lower())
        day = (d + day) % 7
        week_day = ", " + days[day].capitalize()

    if hour > 12:
        hour -= 12
        ampm = "PM"
    
    if ampm == "AM" and hour == 0: hour = 12
    
    if d_pass == 0:
        out+= "{0}:{1} {2}{3}".format(hour, "0" * (2 - len(str(m))) + str(m), ampm, week_day)

        if start[1] == ampm and hour > 12:
            out += " (next day)"
        elif start[1] == "PM" and ampm == "AM":
            out += " (next day)"

    elif d_pass == 1:
        out = "{0}:{1} {2}{3} ({4} days later)".format(hour, "0" * (2 - len(str(m))) + str(m), ampm, week_day, 2)

    else:
        out = "{0}:{1} {2}{3} ({4} days later)".format(hour, "0" * (2 - len(str(m))) + str(m), ampm, week_day, d)

    return out
