def add_time(start, duration, day=0):
    # get the hour
    start_hour = int(start.split(":")[0])
    duration_hour = int(duration.split(":")[0])

    # get the minute
    start_minute = int(start.split(":")[1][:2])
    duration_minute = int(duration.split(":")[1][:2])

    # get AM/PM
    clock = start.split(":")[1][3:]

    # Add minutes
    new_minute = start_minute + duration_minute

    # Add hours
    new_hour = new_minute // 60 + start_hour + duration_hour

    # Trim minutes over an hour (60)
    new_minute = new_minute % 60
    if new_minute < 10:
        new_minute = ''.join(('0', str(new_minute)))

    # Convert to 24 for hour calculations
    if clock == 'PM':
        new_hour += 12

    new_time = ''
    if new_hour >= 12:
        days = new_hour // 24
        if new_hour % 24 >= 12:
            clock = 'PM'
        else:
            clock = 'AM'
        new_hour = new_hour % 12
        if new_hour == 0:
            new_hour = 12

        if days == 1:
            new_time += f' (next day)'
        elif days > 1:
            new_time += f' ({days} days later)'

        if day != 0:
            day_list = ['monday', 'tuesday', 'wednesday', 'thurdsay', 'friday', 'saturday', 'sunday']

            index = day_list.index(day.casefold())
            day = day_list[(index + days) % 7]
            new_time = ''.join((f', {day.capitalize()}', new_time))

    new_time = ''.join((f'{new_hour}:{new_minute} {clock}', new_time))
    return new_time
