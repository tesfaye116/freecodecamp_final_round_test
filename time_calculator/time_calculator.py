def add_time(start, duration, day=None):

    start_time = start.split()
    start_time_hour = int(start_time[0].split(':')[0])
    start_time_min = int(start_time[0].split(':')[1])
    start_time_ampm = start_time[1]

    duration_time = duration.split(':')
    duration_time_hour = int(duration_time[0])
    duration_time_min = int(duration_time[1])

    new_time_hour = start_time_hour + duration_time_hour
    new_time_min = start_time_min + duration_time_min

    if new_time_min >= 60:
        new_time_hour += 1
        new_time_min -= 60
        if new_time_min < 10:
            new_time_min = '0' + str(new_time_min)

    if new_time_hour > 12:
        new_time_hour -= 12
        if start_time_ampm == 'AM':
            start_time_ampm = 'PM'
        else:
            start_time_ampm = 'AM'

    if day is not None:
        new_time = str(new_time_hour) + ':' + \
            str(new_time_min) + ' ' + start_time_ampm + ', ' + day.capitalize()
    else:
        new_time = str(new_time_hour) + ':' + \
            str(new_time_min) + ' ' + start_time_ampm

    return new_time
